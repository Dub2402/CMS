from .Parser import Parser

from pick import pick
from dublib.Methods.JSON import ReadJSON
import os 


class Pick_Objects:

    def __GetConfigs(self) -> list:
        self.__Configs = list()
        for file in os.listdir("Config"):
            self.__Configs.append(ReadJSON(f"Config/{file}"))

        return self.__Configs
    
    def __GetConfig(self, site) -> dict:
        for Index in range(len(self.__Configs)):
            if self.__Configs[Index]["name"] == site:
                self.Config = self.__Configs[Index]

        return self.Config

    def __GetNamesSites(self):
        answers = list()
        for Index in range(len(self.__Configs)):
            answers.append(self.__Configs[Index]["name"])
    
        return answers
    
    def __GetNamesSocialNetworks(self, site):
        answers = list()
        for Index in range(len(self.__Configs)):
            if self.__Configs[Index]["name"] == site:
                for key in self.__Configs[Index]["sites"]:
                    answers.append(key)
    
        return answers

    def __init__(self):
        self.__Configs = self.__GetConfigs()
        self.__parser = Parser()

        self.__objects = {
            "1": {
                "title": "Выберите сайт, в котором необходимо изменить ссылку: ",
                "values": [
                    "Выход"
                ]
            },
            "2": {
                "title": "Выберите социальную сеть, для которой необходимо изменить ссылку: ",
                "values": [
                    "Назад"
                ]
            },
            "3": {
                "title": "Текущая ссылка: www.site.com",
                "values": [
                    "Заменить ссылку",
                    "Назад"
                ]
            },
            "4": {
                "title": "Cсылка успешно установлена!",
                "values": [
                    "Назад",
                    "К сайтам",
                    "Выход"
                ]
            }
        }
        
    def Call(self, level: str, site: str = "", social_network: str = "" ):
        title = self.__objects[level]["title"]
        
        if level == "1": answers = self.__GetNamesSites()
        if level == "2": answers = self.__GetNamesSocialNetworks(site)
        if level == "3": 
            replace_link = self.__parser.GetLink(self.__GetConfig(site), social_network)
            print(replace_link)
            title = title.replace("www.site.com", replace_link)

        answers.extend(self.__objects[level]["values"])
        
        answer = pick(answers, title)[0]
        
        return answer






    
    