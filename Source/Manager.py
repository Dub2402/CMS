from .Parser import Parser
from pick import pick
from dublib.Methods.JSON import ReadJSON

import os 

class Manager:

    def __GetConfigs(self) -> list:
        self.__Configs = list()
        for file in sorted(os.listdir("Config")):
            self.__Configs.append(ReadJSON(f"Config/{file}"))

        return self.__Configs
    
    def __GetConfigSite(self, site) -> dict:
        for Index in range(len(self.__Configs)):
            if self.__Configs[Index]["name"] == site:
                self.ConfigSite = self.__Configs[Index]

        return self.ConfigSite
    

    def __GetMount(self, site, social_network) -> str:
        self.ConfigSite =self.__GetConfigSite(site)
        for key in self.ConfigSite["sites"]:
            if key == social_network: 
                path = f"{self.ConfigSite["mount"]}"

        return path


    def __GetConfigSiteSocialNetwork(self, site, social_network) -> dict:
        self.ConfigSite = self.__GetConfigSite(site)
        for key in self.ConfigSite["sites"]:
            if key == social_network: 
                self.ConfigSiteSocialNetwork = self.ConfigSite["sites"][key]

        return self.ConfigSiteSocialNetwork


    def __GetNamesSites(self) -> list:
        answers = list()

        for Index in range(len(self.__Configs)):
            answers.append(self.__Configs[Index]["name"])
    
        return answers
    
    def __GetNamesSocialNetworks(self, site) -> list:
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
                "title": "Выберите сайт, в котором необходимо изменить ссылку:",
                "values": [
                    "Выход"
                ]
            },
            "2": {
                "title": "Выберите сервис, для которого необходимо изменить ссылку:",
                "values": [
                    "Назад"
                ]
            },
            "3": {
                "title": "Текущая ссылка: ",
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
        
    def Call(self, level: str, site: str = "", social_network: str = "", link: str = ""):
        title = self.__objects[level]["title"]
        
        if level == "1": 
            answers = self.__GetNamesSites()
            answers.extend(self.__objects[level]["values"])

        if level == "2": 
            answers = self.__GetNamesSocialNetworks(site)
            answers.extend(self.__objects[level]["values"])

        if level == "3": 
            self.replace_link = self.__parser.GetLink(self.__GetConfigSiteSocialNetwork(site, social_network), self.__GetMount(site, social_network))
            title += self.replace_link
            answers = self.__objects[level]["values"]
    
        if level == "4": 
            self.__parser.ReplaceLink(self.__GetConfigSiteSocialNetwork(site, social_network), self.__GetMount(site, social_network), link, self.replace_link)
            answers = self.__objects[level]["values"]

        answer = pick(answers, title)[0]
        
        return answer






    
    