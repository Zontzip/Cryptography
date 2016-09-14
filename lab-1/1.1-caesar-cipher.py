# Date created: 2016-09-13 
# Authour: Alex Kiernan
# Contents: Caesar cipher implementation

#import pdb

# pass in the msg, key and optional decrypt (default is False)
def caesar(string, key, decrypt=False):
	#pdb.set_trace()

	# if true, the algorithm will be reversed
	if decrypt: 
		key = 26 - key

	encrypted_msg = ""
	# 1. Loop through each letter in the string.
	# 2. Check if letter is between A - Z (65 - 90)
	# 	 or else is between a - z (97 - 122).
	# 3. If character is between either of these than append a random letter 
	#    that is between either 65 - 90 or 97 - 122 to the encrypted_msg string.
	# For example, h (ascii 104) would enter the second "if" and the character 
	# x (ascii 120) would be added to the encrypted_msg string.
	for letter in string:
		# ord() returns the ascii representation of a character
		if(ord(letter) >= 65 and ord(letter) <= 90):
			# chr() is the opposite of ord(), returns a character
			encrypted_msg += chr((ord(letter) - 65 + key) % 26 + 65)
		elif(ord(letter) >= 97 and ord(letter) <= 122):
			encrypted_msg += chr((ord(letter) - 97 + key) % 26 + 97)
		# else do not encrypt the letter
		else:
			encrypted_msg += letter
	return encrypted_msg

def encrypt(unencrypted_msg, key):
	return caesar(unencrypted_msg, key)

def decrypt(c, key):
	return caesar(c, key, True)	

# Pass in message and number of places to shift each letter
msg = encrypt("hello alex", 16)
print msg

print decrypt(msg, 16)