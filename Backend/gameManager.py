from coord import Coord
from piece import Piece
from game import Game

class gameManager:
    def __init__(self):
        self.games = {}

    def addGame(self, id):
        self.games[id] = Game()
    
    def removeGame(self, id):
        del self.games[id]

    def getGame(self, id):
        return self.games[id]

