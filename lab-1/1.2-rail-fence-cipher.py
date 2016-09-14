# Date created: 2016-09-13 
# Authour: Alex Kiernan
# Contents: Rail fence cipher implementation
import pdb

def fence(msg, key):
	pdb.set_trace()
	# Create 2D array of size [key] of arrays of size [msg] 
	# which forms the fence
	fence = [[None] * len(msg) for n in range(key)]
	# Create array of values corresponding to the range of the key - 1 and 
	# the range of values of the key - 1 to 0 with a step down of - 1
	rails = range(key - 1) + range(key - 1, 0, -1)

	# enumerate returns an enumerate object which is a number corresponding 
	# to each letter in the msg
	for n, x in enumerate(msg):
		# fill in the 2D array with the msg
		fence[rails[n % len(rails)]][n] = x

	return [c for rail in fence for c in rail if c is not None]

def encrypt(msg, key):
	return ''.join(fence(msg, key))

def decrypt(c, key):
	rng = range(len(c))
	pos = fence(rng, key)
	return ''.join(c[pos.index(key)] for key in rng)

# Encrypt a message with a fence of n
f = encrypt("Hello", 3)
print f

print decrypt(f, 3)
