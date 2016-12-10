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

if __name__ == "__main__":
    print("Entropy Test Using NIST Test 01 - Frequency of Bits")

    try:
        print("\nOpening data file...")
        with open("data.txt") as f:
            content = f.readlines()
        print("Data file opened!")
    except:
        print("Error opening data file")

    # p-value threshold is 0.005
    for binary_string in content:
        p_value = monobit(binary_string)
        print ("\nBinary string: " + binary_string + "p-value:  "
        + str(p_value))
