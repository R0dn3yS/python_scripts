import os
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

option = input("1. Generate new keypair \n2. Encrypt string to file \n3. Decrypt file to string \nOption: ")

def RSA_choice():
	if option == "1":
		# Create keys directory
		if os.path.exists("./keys"):
			pass
		else:
			os.mkdir("./keys")

		# Generate Keys
		key = RSA.generate(2048, e=65537)

		# Create and export private key
		private_key = key.export_key()
		file_out = open("keys/private.pem", "wb")
		file_out.write(private_key)
		file_out.close()

		# Create and export public key
		public_key = key.publickey().export_key()
		file_out = open("keys/public.pem", "wb")
		file_out.write(public_key)
		file_out.close()
	elif option == "2":
		data = input("Data to encrypt: ").encode("utf-8")
		encFile = input("Filename for encrypted data: ")
		file_out = open(encFile + ".bin", "wb")

		public_key = RSA.import_key(open("keys/public.pem").read())
		session_key = get_random_bytes(16)

		# Encrypt the session key with the public RSA key
		cipher_rsa = PKCS1_OAEP.new(public_key)
		enc_session_key = cipher_rsa.encrypt(session_key)

		# Encrypt the data with the AES session key
		cipher_aes = AES.new(session_key, AES.MODE_EAX)
		ciphertext, tag = cipher_aes.encrypt_and_digest(data)
		[ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
		file_out.close()
	elif option == "3":
		encFile = input("File to decrypt: ")
		file_in = open(encFile, "rb")

		private_key = RSA.import_key(open("keys/private.pem").read())

		enc_session_key, nonce, tag, ciphertext = \
			[ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

		# Decrypt the session key with the private RSA key
		cipher_rsa = PKCS1_OAEP.new(private_key)
		session_key = cipher_rsa.decrypt(enc_session_key)

		# Decrypt the data with the AES session key
		cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
		data = cipher_aes.decrypt_and_verify(ciphertext, tag)
		print(data.decode("utf-8"))
	else:
		RSA_choice()

RSA_choice()