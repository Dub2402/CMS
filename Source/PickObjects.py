from pick import pick
from dublib.Methods.JSON import ReadJSON

class Pick_Objects:

	def __GetNamesSites(self, site):
		self.Data = ReadJSON(f"Data/{site}.json")
	   
		NameSites = set()
		answers = list()
		for Index in range(len(self.Data["files"])):
			for key in self.Data["files"][Index]:         
				if key == "path": NameSites.add(key.replace("path", "Назад"))
				else: NameSites.add(key)
				
		answers = sorted(NameSites)
		return answers

	def __init__(self):
		self.__objects = {
			"1": {
				"title": "Выберите сайт, в котором необходимо изменить ссылку: ",
				"values": [
					"Основной",
					"AnnaMagik",
					"4(ENG)",
					"4(RUS)",
					"5", 
					"Выход"
				]
			},
			"2": {
				"title": "Выберите социальную сеть, для которой необходимо изменить ссылку: ",
				"values": [
					"WhatsApp",
					"Telegram",
					"TikTok",
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
		
	def Call(self, level: str, site: str = "", titlereplace: str = ""):
		title = self.__objects[level]["title"]
		answers = self.__objects[level]["values"]
		if level == "2": answers = self.__GetNamesSites(site)
		if level == "3": title = title.replace("www.site.com", titlereplace)
		
		answer = pick(answers, title)[0]
		
		return answer






	
	