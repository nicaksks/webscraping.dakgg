from util.constants import SEASON_ID
from datetime import datetime

class Util:
    def __init__(self) -> None:
        self.__baseURL = "https://dak.gg/er"

    def format_url(self, *var) -> str:
        path: str = var[0]
        
        for i, v in enumerate(var[1:], start=1):
            path = path.replace("{" + str(i) + "}", v)
        
        return "{}/{}".format(self.__baseURL, path)

    def seasons_ids(self) -> str:
        seasons: list = map(str, list(SEASON_ID.keys()))
        return ", ".join(seasons)

    def date_time(self) -> str:
        return datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
    
    def format_elo(self, data: list) -> tuple:
        
        lp: int = 0
        division: int = 0
            
        if data[2] == "-":
            lp = data[3]
            division = data[1]
        else:
            lp = data[2]
            division = 1
            
        return (data[0], division, lp)
    
    def format_element(self, element: str, id: int) -> str:
        return element.replace("{0}", str(id))