class Player:
    def __init__(self, nickname = "", score: int = 0):
        self.nickname = nickname
        self.score = score

    def setScore(self, score):
        self.__score = score
    
    def setNickName(self, nn):
        self.__nickname = nn
    
    def getScore(self):
        return self.__score
    
    def getNickName(self):
        return self.__nickname
    
    def __str__(self):
        return "User: {}, Score: {}".format(self.nickname, self.score)
    