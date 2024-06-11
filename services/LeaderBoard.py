from services.Dak import Dak
from util.constants import TEAM_MODE, CURRENT_SEASON, ELEMENTS, SEASON_ID, SERVER_NAME, PATHS

class LeaderBoard(Dak):
    def __init__(self, teamMode: str = TEAM_MODE, seasonId: int = CURRENT_SEASON, serverName: str = "SaoPaulo", limit: int = 100) -> None:
        super().__init__()

        self.__teamMode = teamMode.upper()
        if self.__teamMode != TEAM_MODE:
            raise Exception(
                f"{self.__teamMode} não é um modo de jogo válido. Modo de jogo disponível: {TEAM_MODE}")

        self.__seasonId = int(seasonId)
        if not self.__seasonId in SEASON_ID:
            raise Exception(f"Season id {self.__seasonId} inválida. Seasons ids disponíveis: {self.seasons_ids()}")

        self.__serverName = serverName.lower().title()
        if not self.__serverName in SERVER_NAME:
            raise Exception(f"{self.__serverName} não é um servidor válido. Servidores disponíveis: {", ".join(SERVER_NAME)}")

        self.__limit = limit
        if  type(self.__limit) != "int" or self.__limit >= 100:
            self.__limit = 100
                    
        self.__players: list = []
        self.__show()

    def __show(self) -> None:
        self._browser.get(self.format_url(PATHS["LEADERBOARD"], self.__teamMode, SEASON_ID[self.__seasonId], self.__serverName))
        try:
            for i in range(1, self.__limit + 1):
                self.__body(i)
            self.exit()
            self._csv.save("leaderboard", self.__players)
        except:
            self.exit()

    def __ranking(self, id: int) -> int:
        return self.wait(self.format_element(ELEMENTS["LEADERBOARD"]["RANKING"], id)).text

    def __player_name(self, id: int) -> str:
        return self.wait(self.format_element(ELEMENTS["LEADERBOARD"]["PLAYERNAME"], id)).text

    def __elo(self, id: int) -> tuple:
        data = self.wait(self.format_element(ELEMENTS["LEADERBOARD"]["ELO"], id)).text
        ranking = data.split(" ")
        
        if len(ranking) <= 1:
            return ranking[0], 1
        
        return ranking[0], ranking[1]

    def __lp(self, id: int) -> int:
        return self.wait(self.format_element(ELEMENTS["LEADERBOARD"]["LP"], id)).text.replace(" RP", "")

    def __winrate(self, id: int) -> float:
        return self.wait(self.format_element(ELEMENTS["LEADERBOARD"]["WINRATE"], id)).text.replace("%", "")

    def __top3(self, id: int) -> float:
        return self.wait(self.format_element(ELEMENTS["LEADERBOARD"]["TOP3"], id)).text.replace("%", "")

    def __games_played(self, id: int) -> int:
        return self.wait(self.format_element(ELEMENTS["LEADERBOARD"]["GAMESPLAYED"], id)).text

    def __avgrank(self, id: int) -> float:
        return self.wait(self.format_element(ELEMENTS["LEADERBOARD"]["AVGRANK"], id)).text.replace("#", "")

    def __avgkills(self, id: int) -> float:
        return self.wait(self.format_element(ELEMENTS["LEADERBOARD"]["AVGKILLS"], id)).text

    def __body(self, id: int) -> None:
        elo, division  = self.__elo(id)
        self.__players.append({
            "ranking": self.__ranking(id),
            "player_name": self.__player_name(id),
            "elo": elo,
            "division": division,
            "lp": self.__lp(id),
            "winrate": self.__winrate(id),
            "games_played": self.__games_played(id),
            "top3": self.__top3(id),
            "avgrank": self.__avgrank(id),
            "avgkills": self.__avgkills(id)
        })