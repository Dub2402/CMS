from dublib.Methods.JSON import ReadJSON
from bs4 import BeautifulSoup


class Parser:

    def __init__(self) -> None:
        pass
        
    def GetLink(self, config: dict, social_network: str):
        titlereplace = ""

        for key in config["sites"]:
            if key == social_network: 
                path = f"{config["mount"]}" + f"{config["sites"][key]["files"][0]}"
                with open(path) as file:
                    soup = BeautifulSoup(file, "html.parser")
                    if config["sites"][social_network]["property"] == "class":
                
                            titlereplace = soup.find(class_ = config["sites"][social_network]["value"]).attrs['href']

        return titlereplace
    
    def ReplaceLink():
        pass