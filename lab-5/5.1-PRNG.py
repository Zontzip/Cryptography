MT = [0 for i in xrange(624)]
index = 0

bitmask_1 = (2 ** 32) - 1

bitmask_2 = 2 ** 31

bitmask_3 = (2 ** 31) - 1

def initialize_generator(seed):
    global MT
    global bitmask_1
    MT[0] = seed
    for i in xrange(1,624):
        MT[i] = ((1812433253 * MT[i-1]) ^ ((MT[i-1] >> 30) + i)) & bitmask_1


def extract_number():
    global index
    global MT
    if index == 0:
        generate_numbers()
    y = MT[index]
    y ^= y >> 11
    y ^= (y << 7) & 2636928640
    y ^= (y << 15) & 4022730752
    y ^= y >> 18

    index = (index + 1) % 624
    return y

def generate_numbers():
    global MT
    for i in xrange(624):
        y = (MT[i] & bitmask_2) + (MT[(i + 1 ) % 624] & bitmask_3)
        MT[i] = MT[(i + 397) % 624] ^ (y >> 1)
        if y % 2 != 0:
            MT[i] ^= 2567483615

if __name__ == "__main__":
    from datetime import datetime
    now = datetime.now()
    initialize_generator(now.microsecond)
    for i in xrange(100):
        print extract_number()