import hashlib
import hmac
from hashlib import md5

if __name__ == "__main__":
    key = "BIANCHI"
    plaintext = "AAAABBBBCCCCD"
    hash_value = hmac.new(key, plaintext, md5).hexdigest()

    print hash_value
    
    # Compare the digests
    print hmac.compare_digest(hmac.new(key, plaintext, md5).hexdigest(), hash_value)