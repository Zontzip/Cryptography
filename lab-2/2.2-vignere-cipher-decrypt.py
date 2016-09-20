# Date created: 2016-09-20
# Authour: Alex Kiernan
# Contents: Decrypt ciphertext using Vignere cipher

from itertools import starmap, cycle
 
def decrypt(message, key):
 
    # single letter decryption.
    def dec(c,k): return chr(((ord(c) - ord(k) - 2*ord('A')) % 26) + ord('A'))
 
    return "".join(starmap(dec, zip(message, cycle(key))))

encrypted_msg = open("msg2.txt", 'r').read()
encrypted_msg = filter(str.isalpha, encrypted_msg.upper())
key = "FACEBOOKPASSWORD"

decrypted_msg = decrypt(encrypted_msg, key)

print "Encrypted message: " + encrypted_msg 
print "\nDecrypted message: " +decrypted_msg