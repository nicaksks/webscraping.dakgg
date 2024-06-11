# WebScrapping | Dak.gg
Aprendendo um pouco de **selenium** e tirando a **ferrugem do Python**<br>

Projeto para pegar os dados da **Leaderboard** e do **Perfil** de determinado jogador do jogo **Eternal Return**. <br>
Os dados são coletados do site **[Dak.gg](https://dak.gg/er/leaderboard)**

# Iniciando
Você pode chamar a classe **Leaderboard** ou **Profile**. ambas as classes possui parametros opcionais.
* **Leaderboard** - Modo de jogo, Season Id, Nome do Servidor,  Quantidade de jogadores 1~100,
* **Profile** - Nickname do jogador **(obrigatório)**, Nome do servidor
* Você pode visualizar quais dados são passados em **./util/constants.py** ou passar qualquer valor em campo **opcional** que vai retornar os valores que podem ser passados.

Depois iniciar uma das classes, uma pasta chamada **files** vai ser criada e dentro dessa pasta vai ser salvo as informações do **jogador(es)** em um arquivo **.csv**<br>
O nome do arquivo é o nome da classe mais a data e hora.