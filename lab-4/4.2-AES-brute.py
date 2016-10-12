from Crypto.Cipher import AES

ciphertext_base_16 = "43D3215C92A75A1478FCF9CB950D20DB"

def pad(plaintext):
	return Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='CMS')

def unpad(padded_plaintext):
	return Padding.removePadding(padded_plaintext,mode='CMS')

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

ciphertext_base_16 = ciphertext_base_16.decode('hex')

with open('keys.txt') as file:
	keys = file.read().splitlines()
file.closed

for key in keys:
	aes = AES.new(key, AES.MODE_ECB)
	decrypted_msg = aes.decrypt(ciphertext_base_16)
	if is_ascii(decrypted_msg):
		print("Decrypted message with key " + key + ": "+ decrypted_msg)