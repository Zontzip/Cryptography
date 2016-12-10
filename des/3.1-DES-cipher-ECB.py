# -*- coding: utf-8 -*-

from Crypto.Cipher import DES
	
key = "12345678"
plain_text = "AAAABBBBAAAABBBB"
cipher_text = "19FF4637BB2FE77C19FF4637BB2FE77C"

des = DES.new(key, DES.MODE_ECB)
encrypted_msg = des.encrypt(plain_text)
encrypted_msg = encrypted_msg.encode('hex')
print(encrypted_msg)

encrypted_msg = encrypted_msg.decode('hex')
decrypted_msg = des.decrypt(encrypted_msg)
print(decrypted_msg)
