from OpenSSL import crypto, SSL

# Generate a new private key
private_key = crypto.PKey()
private_key.generate_key(crypto.TYPE_RSA, 2048)

# Create a self-signed certificate
cert = crypto.X509()
cert.get_subject().CN = 'api.openai.com'
cert.set_serial_number(1000)
cert.gmtime_adj_notBefore(0)
cert.gmtime_adj_notAfter(315360000) # valid for 10 years
cert.set_issuer(cert.get_subject())
cert.set_pubkey(private_key)
cert.sign(private_key, 'sha256')

# Write the private key and certificate to disk
with open("private_key.pem", "wb") as key_file:
    key_file.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, private_key))
with open("certificate.pem", "wb") as cert_file:
    cert_file.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))