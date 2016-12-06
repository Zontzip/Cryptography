from Crypto.Cipher import DES
import Padding
import base64

def pad(plaintext):
	return Padding.appendPadding(plaintext,blocksize=Padding.DES_blocksize,mode='CMS')

def unpad(padded_plaintext):
	return Padding.removePadding(padded_plaintext,mode='CMS')

def parts(longdata, n):
    for i in range(8, len(longdata),n):
        yield longdata[i:i +n]

if __name__ == "__main__":
    key = "12345678"
    plaintext = "AAAABBBBCCCC"
    plaintext_with_padding = "AAAABBBBCCCC\x00\x0004"
    hash_base_16 = "4358995013B4B1F8"
    
    padded_plaintext = pad(plaintext)

    message = dict(enumerate(list(parts(padded_plaintext, 8)), start = 0))

    for e in message:
        des = DES.new(message[e], DES.MODE_ECB)
        cipher_text = des.encrypt(hash_base_16)
        hash_base_16 = "".join(chr(ord(x) ^ ord(y)) for x ,y in zip(hash_base_16, cipher_text))

    print "Padded plaintext: " + padded_plaintext
    print "Encoded hash: " + str(map(''.join, zip(*[iter(base64.b16encode(hash_base_16))]*16)))