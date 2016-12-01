import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2- temp1* x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair(p, q):
    # Error checking for primes
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    # 2 - Calculate the modulus
    n = p * q

    # 3 - Calculate the totient, written as phi
    phi = (p-1) * (q-1)

    # 4.1 - Choose a number e coprime to phi
    e = random.randrange(1, phi)

    # 4.2 - Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # 5 - Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    # Encrypt each letter in plaintext using formula c = m^e mod n
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    # Decrypt each letter in plaintext using formula p = c^d mod n
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

if __name__ == '__main__':
    print ("RSA Encrypter/Decrypter")

    # 1 - Prime numbers p, q
    p = 17
    q = 23

    print ("\nGenerating public/private keypairs...")
    public, private = generate_keypair(p, q)
    print("\n****************************")
    print("Public key is:" + str(public))
    print("Private key is:" + str(private))
    print("****************************\n")
    # Get user plaintext
    message = raw_input("Enter a message to encrypt with private key: ")
    # Encrypt message
    encrypted_msg = encrypt(private, message)
    print ("\nEncrypted message is: ")
    print (''.join(map(lambda x: str(x), encrypted_msg)))
    # Decrypt message
    print ("\nDecrypted message is:")
    print (decrypt(public, encrypted_msg))
