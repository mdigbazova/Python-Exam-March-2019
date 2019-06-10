#L = [(k, v) for (k, v) in dictServers.items ()]
#L1 = [v for (k, v) in dictServers.items ()]
# L1 = [v for (k, v) in dictServers.items()]
# servers_with_lec = list(filter(lambda srv: l_name in srv.lectures, L1))

class Player:
    def __init__(self, pName, listGames):
        self.pName = pName
        self.setProps(listGames)

    @property
    def pName(self):
        return self.__pName

    @pName.setter  # setter
    def pName(self, pName):
        self.__pName = pName

    def setProps(self, listGames):
        self.score = sum(listGames)
        self.numGames = len(listGames)


def print_list(sorted_names, elem):
    for player in sorted_names:
        name = player.pName
        if elem == 'score':
            elem2Print = player.score
        else:
            elem2Print = player.numGames
        print(f"{name}: {elem2Print}")


listPlayers = []
tupleScores = []
tupleCountGames = []

data = input()

while data != 'report':
    #{playerName} -> {resultOfTheGame}, {resultOfTheGame}, {resultOfTheGame}, {resultOfTheGame}

    pName = data.split(' -> ')[0]
    gamesList = list(map(int, data.split(' -> ')[1].split(', ')))
    player = Player(pName, gamesList)
    listPlayers.append(player)

    data = input ()


#     • score descending
#     • score ascending
#     • numberOfGames descending
#     • numberOfGames ascending

data = input()
while data != 'end':
    if data == 'score descending':
        # {name}: {score}
        sorted_desc_score = sorted (listPlayers, key=lambda player: (-player.score, player.pName))
        print_list(sorted_desc_score, 'score')

    elif data == 'score ascending':
        sorted_asc_score = sorted (listPlayers, key=lambda player: (player.score, player.pName))
        print_list(sorted_asc_score, 'score')

    elif data == 'numberOfGames descending':
        sorted_desc_games = sorted (listPlayers, key=lambda player: (-player.numGames, player.pName))
        print_list(sorted_desc_games, 'numGames')

    else:
        # numberOfGames ascending
        sorted_asc_games = sorted (listPlayers, key=lambda player: (player.numGames, player.pName))
        print_list(sorted_asc_games, 'numGames')


    data = input()


