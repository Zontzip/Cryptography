import sys

def KSA(key):
    keylength = len(key)

    S = range(256)

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]

    return S

def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap

        K = S[(S[i] + S[j]) % 256]
        yield K

def RC4(key):
    S = KSA(key)
    return PRGA(S)

def convert_key(s):
    return [ord(c) for c in s]

print("Stream Cipher Encrpyter")

key = "Secret"
plaintext = "Attack at dawn"

print("\nKey: " + key)
print("Plaintext: " + plaintext)

key = convert_key(key)
keystream = RC4(key)

print("\nCiphertext: ")
for char in plaintext:
    sys.stdout.write("%02X" % (ord(char) ^ keystream.next()))
print
