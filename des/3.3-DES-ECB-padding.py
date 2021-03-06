from Crypto.Cipher import DES
import Padding

key = "12345678"
plaintext = "AAAABBBBCCCC"
plaintext_with_padding = "AAAABBBBCCCC\x00\x0004"
ciphertext_base_16 = "19FF4637BB2FE77C81987E5CB99B66E2"

def pad(plaintext):
	return Padding.appendPadding(plaintext,blocksize=Padding.DES_blocksize,mode='CMS')


def unpad(padded_plaintext):
	return Padding.removePadding(padded_plaintext,mode='CMS')

print("Plaintext: " + plaintext)

padded_plaintext = pad(plaintext)
print("Padded plaintext: " + padded_plaintext)

des = DES.new(key, DES.MODE_ECB)
encrypted_msg = des.encrypt(padded_plaintext)
encrypted_msg = encrypted_msg.encode('hex')
print("Encrypted message: " + encrypted_msg)

encrypted_msg = encrypted_msg.decode('hex')
decrypted_msg = des.decrypt(encrypted_msg)
print("Decrypted message: " + decrypted_msg)

unpadded_plaintext = unpad(padded_plaintext)
print("Unpadded message: " + unpadded_plaintext)
