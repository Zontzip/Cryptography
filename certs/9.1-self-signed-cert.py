from OpenSSL import crypto, SSL
from socket import gethostname
from pprint import pprint
from time import gmtime, mktime

CERT_FILE = "root-cert.pem"
KEY_FILE = "root-private.key"

def create_self_signed_cert():

    # 1 - Generate a 2048-bit (recommended) RSA private key pair
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)

    # 2, 3 - Create CSR and create a X.509 self signed root certificate
    cert = crypto.X509()
    cert.get_subject().C = "IE"
    cert.get_subject().ST = "Dublin"
    cert.get_subject().L = "Blackrock"
    cert.get_subject().O = "DIT"
    cert.get_subject().OU = "DIT"
    cert.get_subject().CN = "alex-kiernan.com"
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10*365*24*60*60)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(key)
    cert.sign(key, 'sha1')

    open(CERT_FILE, "wt").write(
        crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
    open(KEY_FILE, "wt").write(
        crypto.dump_privatekey(crypto.FILETYPE_PEM, key))

if __name__ == "__main__":
    create_self_signed_cert()
