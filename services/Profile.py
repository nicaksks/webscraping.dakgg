from services.Dak import Dak
from util.constants import ELEMENTS, PATHS, SEASON_ID, CURRENT_SEASON
from typing import Union

class Profile(Dak):
    def __init__(self, playerName: str, seasonId: int = CURRENT_SEASON) -> None:
        super().__init__()
        self.__playerName = playerName.lower()
        
        self.__seasonId = int(seasonId)
        if not self.__seasonId in SEASON_ID:
            raise Exception(f"Season id {self.__seasonId} inválida. Seasons ids disponíveis: {self.seasons_ids()}")
        
        self.__url = self.format_url(PATHS["PROFILE"], self.__playerName, SEASON_ID[self.__seasonId])
        self.__show()

    def __show(self) -> None:
        try: 
            self._browser.get(self.__url)
            self._csv.save("profile", self.__body())
            
            return self.exit()
        except:
            self.exit()
            raise Exception(f"{self.__playerName} não foi encontrado. Tente outro nickname.")

    def __body(self) -> list:
        elo, division, lp = self.__elo()
        return [{
            "player_name": self.__playerName,
            "level": self.__level(),
            "elo": elo,
            "division": division,
            "lp": lp,
            "tk": self.__teamKill(),
            "winrate": self.__winrate(),
            "games_played": self.__games_played()
        }]
        
    def __level(self) -> str:
        data = self.wait(ELEMENTS["PROFILE"]["LEVEL"]).text
        return data.split(" ")[1]

    def __elo(self) -> tuple:
        try:
            data = self.wait(ELEMENTS["PROFILE"]["ELO"]).text             
            elo, division, lp = self.format_elo(data.split(" ")) 
            return (elo, division, lp)
        except:
            return ("Sem elo", 0, 0)

    def __teamKill(self) -> Union[int, str]:
        return self.wait(ELEMENTS["PROFILE"]["TK"]).text.replace("-", "0")

    def __winrate(self) -> Union[float, str]:
        data = self.wait(ELEMENTS["PROFILE"]["WINRATE"]).text
        return data.replace("%", "").replace("-", "0")

    def __games_played(self) -> Union[int, str]:
        data = self.wait(ELEMENTS["PROFILE"]["GAMES"]).text
        return data.replace("%", "").replace("-", "0")

