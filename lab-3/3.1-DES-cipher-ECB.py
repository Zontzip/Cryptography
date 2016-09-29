# -*- coding: utf-8 -*-

from Crypto.Cipher import DES
	
key = "12345678"
plain_text = "AAAABBBBAAAABBBB"
encrypted_msg = "19FF4637BB2FE77C19FF4637BB2FE77C"

des1 = DES.new(key, DES.MODE_ECB)
cipher_text = des.encrypt(plain_text)
print(cipher_text.decode)

des2 = DES.new(key, DES.MODE_ECB)
decrypted_msg = des.decrypt(encrypted_msg)
