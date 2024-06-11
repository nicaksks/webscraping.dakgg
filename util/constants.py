# Jogo atualmente só possui o modo SQUAD;
TEAM_MODE: str = "SQUAD"

# ID de cada Season baseada no Dak.gg;
SEASON_ID: dict = {
    1: "SEASON_10",
    2: "SEASON_11",
    3: "SEASON_12",
    4: "SEASON_13"
}

# Season atual;
CURRENT_SEASON: int = list(SEASON_ID)[-1]

# Nome de cada região;
SERVER_NAME: list = ["Seoul", "Ohio", "Frankurt", "Saopaulo", "Global"]

# Caminho das páginas que eu preciso acessar;
PATHS: dict = {
    "PROFILE": "players/{1}/?season={2}",
    "LEADERBOARD": "leaderboard?teamMode={1}&season={2}&serverName={3}"
}

# Elemento das páginas;
ELEMENTS: dict = {
    "LEADERBOARD": {
      "RANKING": "//*[@id='content-container']/table/tbody/tr[{0}]/td[1]",
      "PLAYERNAME": "//*[@id='content-container']/table/tbody/tr[{0}]/td[2]/div/a",
      "ELO": "//*[@id='content-container']/table/tbody/tr[{0}]/td[3]/div/span",
      "LP": "//*[@id='content-container']/table/tbody/tr[{0}]/td[4]",
      "WINRATE": "//*[@id='content-container']/table/tbody/tr[{0}]/td[5]",
      "TOP3": "//*[@id='content-container']/table/tbody/tr[{0}]/td[6]",
      "GAMESPLAYED": "//*[@id='content-container']/table/tbody/tr[{0}]/td[7]",
      "AVGRANK": "//*[@id='content-container']/table/tbody/tr[{0}]/td[8]",
      "AVGKILLS": "//*[@id='content-container']/table/tbody/tr[{0}]/td[9]"
    },
    "PROFILE": {
        "LEVEL": "//*[@id='content-container']/section/div[1]/div[1]/div[2]/div[1]/span",
        "ELO": "//*[@id='content-container']/div[2]/div[1]/section/div[1]/div/div[1]",
        "TK": "//*[@id='content-container']/div[2]/div[1]/section/div[2]/div[1]/div[2]",
        "WINRATE": "//*[@id='content-container']/div[2]/div[1]/section/div[2]/div[2]/div[2]",
        "GAMES": "//*[@id='content-container']/div[2]/div[1]/section/div[2]/div[3]/div[2]",
        "PLAYER_NOT_FOUND": "//*[@id='__next']/div[1]/div[2]/main/p/span[1]"
    }
}