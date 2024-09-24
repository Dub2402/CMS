from .Manager import Manager
from urllib.parse import urlparse
from dublib.CLI.StyledPrinter import Styles, TextStyler
from dublib.CLI.Templates import Clear

class Terminalyzer:

	def __init__(self) -> None:

		self.__manager = Manager()
		
		self.__level = "1"
		self.__site = ""
		self.__social_network = ""
		self.__link = ""
	
	def Start(self):

		answer = self.__manager.Call(self.__level)

		while True:

			if answer == "Заменить ссылку":
				Site = TextStyler(self.__site, decorations = [Styles.Decorations.Bold])
				Service = TextStyler(self.__social_network, decorations = [Styles.Decorations.Bold])
				new_link = input(f"Символ * для отмены.\nВведите новую ссылку для сервиса {Service} на сайте {Site}: ")

				if new_link.strip() == "*":
					answer = "Назад"

				else:
					parse_link = urlparse(new_link)

					if parse_link.scheme:
						self.__link = new_link
						answer = ""

					else: print(f"Ссылка не соответствует формату URL!")
			
			elif answer == "Назад":
				if self.__level == "4": self.__level = str(int(self.__level) - 1)
				self.__level = str(int(self.__level) - 1)
				answer = self.__manager.Call(self.__level, self.__site)

			elif answer == "К сайтам":
				self.__level = "1"
				answer = self.__manager.Call(self.__level)

			elif answer == "Выход":
				Clear()
				exit(0)

			else:
				if self.__level == "1": self.__site = answer

				if self.__level == "2":
					self.__social_network = answer
						
				self.__level = str(int(self.__level) + 1)
				answer = self.__manager.Call(self.__level, self.__site, self.__social_network, self.__link)