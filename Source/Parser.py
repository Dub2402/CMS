from bs4 import BeautifulSoup
from dublib.Methods.JSON import ReadJSON


class Parser():
    def __init__(self) -> None:
        self.__Settings = ReadJSON("Settings.json")
        self.__soup = self.__Get_html(self.__Settings["Основной"]["path"])

    def __Get_html(self, path_to_file: str):
        with open(path_to_file, 'r') as file:
            data = file.read()
        soup = BeautifulSoup(data, "html.parser")

        return soup
    
    def Get_Social_Networks(self):
        for link in self.__soup.find_all("a"):
            print(link.get('href'))

        
    
