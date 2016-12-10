import base64
import hashlib
import sys

if __name__ == "__main__":
    print("Diffie-Hellman Key Agreement")

    g = 5
    p = 23
    print ("\nAlice and Bob agree prime modulus: " + str(p) + ", base: " + str(g))

    a = 6
    b = 15

    A = (g**a) % p
    B = (g**b) % p
    print ("\nAlice chooses a secret integer: " + str(a))
    print ("Alice sends Bob: " + str(A))

    print ("\nBob chooses a secret integer: " + str(b))
    print ("Bob sends Alice: " + str(B))

    keyA = (B**a) % p
    print ("\nAlice computes: " + str(keyA))
    print ("Key: " + str(hashlib.sha256(str(keyA)).hexdigest()))

    keyB = (A**b) % p
    print ("\nBob computes: " + str(keyB))
    print ("Key: "  + str(hashlib.sha256(str(keyB)).hexdigest()))
