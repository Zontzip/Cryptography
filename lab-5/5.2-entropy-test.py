import math
import scipy.special as spc

def monobit(bin_data):
    count = 0
    # If the char is 0 minus 1, else add 1
    for char in bin_data:
        if char == '0':
            count -= 1
        else:
            count += 1
    # Calculate the p value
    sobs = count / math.sqrt(len(bin_data))
    p_val = spc.erfc(math.fabs(sobs) / math.sqrt(2))
    return p_val

with open("data.txt") as f:
    content = f.readlines()

for binary_string in content:
    p_value = monobit(binary_string)
    print p_value
