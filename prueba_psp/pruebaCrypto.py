from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
key = RSA.generate(2048)
private_key = key.export_key()
file_out = open("private.pem", "wb")
file_out.write(private_key)
file_out.close()

public_key = key.publickey().export_key()
file_out = open("public.pem", "wb")
file_out.write(public_key)
file_out.close()

secret_code = """
hola buenas tardes como estas 
        """.encode("utf-8")

file_out = open("encrypted_data.bin", "wb")

recipient_key = RSA.import_key(open("public.pem").read())
session_key = get_random_bytes(16)

# Encrypt the session key with the public RSA key
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_session_key = cipher_rsa.encrypt(secret_code)

file_out.write(enc_session_key)
file_out.close()

print(public_key)
print(secret_code)

print(private_key)