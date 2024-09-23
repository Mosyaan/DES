from Crypto.Cipher import DES

key = b'12345678'
des = DES.new(key, DES.MODE_ECB)

def fill_spaces(text):
	while len(text) % len(key) != 0:
		text += b'\x00'
	return text

def cipher(text):
	filled_text = fill_spaces(text)
	encrypted_text = des.encrypt(filled_text)
	return encrypted_text

def decipher(encrypted_text):
	text = des.decrypt(encrypted_text).split(b'\x00')[0]
	return text.decode()


if __name__ == '__main__':
	text = bytes(input('Message: '), 'UTF-8')
	encrypted_text = cipher(text)
	decrypted_text = decipher(encrypted_text)
	print(encrypted_text)
	print()
	print(decrypted_text)
	print()
	print(len(encrypted_text))
	print(len(decrypted_text))
