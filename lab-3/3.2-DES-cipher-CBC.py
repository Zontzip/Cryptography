# -*- coding: utf-8 -*-

from Crypto.Cipher import DES
	
key = "12345678"
iv = "00000000"
plain_text = "AAAABBBBAAAABBBB"
cipher_text = "AAC823F6BBE58F9EAF1FE0EB9CA7EB08"

des1 = DES.new(key, DES.MODE_CBC, iv)
encrypted_msg = des1.encrypt(plain_text)
encrypted_msg = encrypted_msg.encode('hex');
print(encrypted_msg)

des2 = DES.new(key, DES.MODE_CBC, iv)
encrypted_msg = encrypted_msg.decode('hex');
decrypted_msg = des2.decrypt(encrypted_msg)
print(decrypted_msg)