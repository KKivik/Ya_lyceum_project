import os
import sys
from cryptography.fernet import Fernet

class No_Flash_Drive(Exception):
	pass

class Decoder:
	def __init__(self, path_to_decode):
		self.drive_letter = "E"  # имя буквы внешнего накопителя
		if self.check_drive():
			self.encrypted_path = path_to_decode #"C:/Data" #что шифровать?
			if os.path.isfile(self.drive_letter + ":/key.txt") == False:
				self.write_key()

			self.key = self.load_key()
			self.walk()
		else:
			raise No_Flash_Drive

	def check_drive(self): #эта функция проверяет вставлен ли вообще флеш-накопитель
		if os.system("cd " + self.drive_letter + ":") == 0: #если там что-то есть
			return True
		else:
			return False

	def write_key(self):
		key = Fernet.generate_key()

		with open(self.drive_letter + ":/key.txt", "wb") as key_file:
			key_file.write(key)

	def load_key(self):
		with open(self.drive_letter + ":/key.txt", "r") as file:
			key = file.read()

		return key

	def encrypt(self, filename, key): # Шифрование файла
		fernet = Fernet(key)

		with open(filename, "rb") as file:
			file_data = file.read()

			encrypted_data = fernet.encrypt(file_data)

			with open(filename, "wb") as file:
				file.write(encrypted_data)

	def decrypt(self, filename, key): # Расшифровка файла
		fernet = Fernet(key)

		with open(filename, "rb") as file:
			file_data = file.read()

		decrypted_data = fernet.decrypt(file_data)

		with open(filename, "wb") as file:
			file.write(decrypted_data)


	def walk(self): #Бегает по директории и шифрует файлs
		names = os.listdir(self.encrypted_path)

		for name in names:
			path = os.path.join(self.encrypted_path, name)
			ext = os.path.splitext(path)

			if os.path.isfile(path):
				self.decrypt(path, self.key)
			else:
				self.walk(path)

Decoder('C:/Users/Ученик/Desktop')


