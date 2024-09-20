from .PickObjects import Pick_Objects
from urllib.parse import urlparse


class Terminalyzer:
    def __init__(self) -> None:
        self.__pick_objects = Pick_Objects()
        self.__level = "1"
        self.__site = ""
        self.__social_network = ""
        self.__link = ""
    
    def Start(self):

        answer = self.__pick_objects.Call(self.__level)

        while True:

            if answer == "Заменить ссылку":
                new_link = input(f"Введите новую ссылку для сайта {self.__site} и социальной сети {self.__social_network}: ")
                parse_link = urlparse(new_link)
                if parse_link.scheme:
                    self.__link = new_link
                    answer = ""
                else:
                    input(f"Ссылка не соответствует формату. Нажмите Enter для новой попытки.")
            
            elif answer == "Назад":
                self.__level = str(int(self.__level)- 1)
                answer = self.__pick_objects.Call(self.__level)

            elif answer == "К сайтам":
                self.__level = "1"
                answer = self.__pick_objects.Call(self.__level)

            elif answer == "Выход":
                exit(0)

            else:
                if self.__level == "1":
                    self.__site = answer

                if self.__level =="2":
                    self.__social_network = answer

                self.__level = str(int(self.__level)+ 1)
                answer = self.__pick_objects.Call(self.__level, self.__site)