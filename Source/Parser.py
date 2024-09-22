from dublib.Methods.JSON import ReadJSON
from bs4 import BeautifulSoup


class Parser:

    def __init__(self) -> None:
        pass
        
    def GetLink(self, site, social_network):
        self.Data = ReadJSON(f"Data/{site}.json")

        for Index in range(len(self.Data["files"])):
            for key in self.Data["files"][Index]:    
                if key == social_network: 
                    with open(self.Data["files"][Index]["path"]) as file:
                        soup = BeautifulSoup(file, "html.parser")
                        if self.Data["files"][Index][key][0]["property"] == "class":
                            titlereplace = soup.find(class_ = self.Data["files"][Index][key][0]["value"]).attrs['href']
                
        return titlereplace
    
    def ReplaceLink():
        pass