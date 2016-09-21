# Date created: 2016-09-20
# Authour: Alex Kiernan
# Contents: Encrypt plaintext with Vignere cipher 

from itertools import starmap, cycle
 
def encrypt(message, key):
 
    # convert to uppercase & strip out non-alpha characters
    message = filter(str.isalpha, message.upper())
 
    def enc(c,k): return chr(((ord(k) + ord(c) - 2*ord('A')) % 26) + ord('A'))
 
    return "".join(starmap(enc, zip(message, cycle(key))))

text = open("msg1.txt", 'r').read()
key = "PASSWORD"

encrypted_msg = encrypt(text, key)

print text
print encrypted_msg 