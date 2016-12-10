from OpenSSL import crypto, SSL
from socket import gethostname
from pprint import pprint
from time import gmtime, mktime

CERT_FILE = "cert.pem"
KEY_FILE = "private.key"

def create_end_user_cert():

    # 1 - Generate a 1024-bit RSA private key pair
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 1024)

    # 2 - Load CA info
    ca_cert = crypto.load_certificate(crypto.FILETYPE_PEM, open("root-cert.pem").read())
    ca_key = crypto.load_privatekey(crypto.FILETYPE_PEM, open("root-private.key").read(), "owtf-dev")

    cert = crypto.X509()
    cert.get_subject().C = "IE"
    cert.get_subject().ST = "Dublin"
    cert.get_subject().L = "Dalkey"
    cert.get_subject().O = "DIT"
    cert.get_subject().OU = "Inbound-Proxy"
    cert.get_subject().CN = "test.com"
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10*365*24*60*60)
    cert.set_issuer(ca_cert.get_subject())
    cert.set_pubkey(key)
    cert.sign(ca_key, 'sha1')

    open(CERT_FILE, "wt").write(
        crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
    open(KEY_FILE, "wt").write(
        crypto.dump_privatekey(crypto.FILETYPE_PEM, key))

if __name__ == "__main__":
    create_end_user_cert()
