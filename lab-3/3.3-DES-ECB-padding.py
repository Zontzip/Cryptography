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

padded_plaintext = pad(plaintext)
print(padded_plaintext)

unpadded_plaintext = unpad(padded_plaintext)
print(unpadded_plaintext)
