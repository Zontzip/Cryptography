from OpenSSL import crypto

def verify_chain_of_trust(cert_pem, trusted_cert_pem):
    certificate = crypto.load_certificate(crypto.FILETYPE_PEM, cert_pem)
    trusted_cert = crypto.load_certificate(crypto.FILETYPE_PEM, trusted_cert_pem)

    store = crypto.X509Store()
    store.add_cert(trusted_cert)
    store_ctx = crypto.X509StoreContext(store, certificate)
    result = store_ctx.verify_certificate()

    if result is None:
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        with open("cert.pem", "r") as cert_file:
            cert = cert_file.read()

        with open("root-cert.pem", "r") as root_cert_file:
            root_cert = root_cert_file.read()
    except IOError:
        print "Cannot open certificate files", arg

    verified = verify_chain_of_trust(cert, root_cert)

    if verified:
        print("Certificate verified")
