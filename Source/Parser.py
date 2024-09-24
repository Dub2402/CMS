from bs4 import BeautifulSoup

class Parser:

    def __init__(self) -> None:
        pass


    def __GetSoup(self, path) -> BeautifulSoup:
        with open(path) as file:
            soup = BeautifulSoup(file, "html.parser")

            return soup
        
    def GetLink(self, config: dict, mount: str):
        titlereplace = ""
        path = f"{mount}{config["files"][0]}"
        soup = self.__GetSoup(path)
        with open(path) as file:
            soup = BeautifulSoup(file, "html.parser")
            if config["property"] == "class":
                titlereplace = soup.find(class_ = config["value"]).attrs['href']

        return titlereplace
    
    def ReplaceLink(self, config: dict, mount: str, new_link: str, old_link: str):
        for Index in range(len(config["files"])):
            path = f"{mount}{config["files"][Index]}"
            with open(path, 'r') as file:
                old_data = file.read()
                new_data = old_data.replace(old_link, new_link)
            with open (path, 'w') as file:
                file.write(new_data)
