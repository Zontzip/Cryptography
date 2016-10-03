# -*- coding: utf-8 -*-

from Crypto.Cipher import DES
	
key = "12345678"
plain_text = "AAAABBBBAAAABBBB"
encrypted_msg = "19FF4637BB2FE77C19FF4637BB2FE77C"

des = DES.new(key, DES.MODE_ECB)
cipher_text = des.encrypt(plain_text)
cipher_text = cipher_text.encode('hex');
print(cipher_text)

cipher_text = cipher_text.decode('hex');
decrypted_msg = des.decrypt(cipher_text)
print(decrypted_msg)
