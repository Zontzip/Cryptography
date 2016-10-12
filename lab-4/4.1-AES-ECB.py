from Crypto.Cipher import AES
import Padding

key = "1234567812345678"
plaintext = "AAAABBBBCCCCDDDDAA"
plaintext_with_padding = "AAAABBBBCCCCDDDDAA\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x0014"
ciphertext_base_16 = "43D3215C92A75A1478FCF9CB950D20DB502A485FD5735486D57AEA9AA809E3DD"

def pad(plaintext):
	return Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='ZeroLen')

def unpad(padded_plaintext):
	return Padding.removePadding(padded_plaintext,mode='ZeroLen')

print("Plaintext: " + plaintext)

padded_plaintext = pad(plaintext)
print("Padded plaintext: " + padded_plaintext.encode('hex'))

aes = AES.new(key, AES.MODE_ECB)
encrypted_msg = aes.encrypt(padded_plaintext)
print("Encrypted message: " + encrypted_msg.encode('hex'))

decrypted_msg = aes.decrypt(encrypted_msg)
print("Decrypted message: " + decrypted_msg)