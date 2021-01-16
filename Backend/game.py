from coord import Coord
from piece import Piece
class Game:
    def __init__(self):
        self.board = [[Piece() for x in range(8)] for y in range(8)]
        pieces = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
        currId = 0
        for i in range(8):
            self.board[0][i] = Piece(pieces[i], 1, currId, 0)
            currId+=1
        for i in range(8):
            self.board[1][i] = Piece("pawn", 1, currId, 0)
            currId+=1
        for i in range(8):
            self.board[6][i] = Piece("pawn", 0, currId, 0)
            currId+=1
        for i in range(8):
            self.board[7][i] = Piece(pieces[i], 0, currId, 0)
            currId+=1
    
    def getPossibleMoves(self, c:Coord):
        if(c.isValid() == False):
            return -1
        p = self.getSquare(c)
        enemyTeam = 0 if p.team==1 else 1
        if p.name == "knight":
            deltas = [
                Coord(1,2),Coord(2,1),
                Coord(-1,2),Coord(-2,1),
                Coord(1,-2),Coord(2,-1),
                Coord(-1,-2),Coord(-2,-1),
            ]
            out = []
            for delta in deltas:
                temp = c+delta
                if(temp.isValid() and self.getSquare(temp).team != p.team):
                    out.append(temp)
            return out
        elif p.name == "king":
            deltas = [
                Coord(-1,0),Coord(-1,-1),
                Coord(0,-1),Coord(1,-1),
                Coord(1,0),Coord(1,1),
                Coord(0,1),Coord(-1,1)
            ]
            out = []
            for delta in deltas:
                temp = c+delta
                if(temp.isValid() and self.getSquare(temp).team != p.team):
                    out.append(temp)
            return out
        elif p.name == "rook":
            deltas = [
                Coord(-1,0),Coord(1,0),
                Coord(0,1),Coord(0,-1)
            ]
            out = []
            for delta in deltas:
                temp = c+delta
                while (temp.isValid() and self.getSquare(temp).team != p.team):
                    if(self.getSquare(temp).team == enemyTeam):
                        out.append(temp)
                        break
                    out.append(temp)
                    temp = temp+delta
            return out
        elif p.name == "bishop":
            deltas = [
                Coord(-1,1),Coord(-1,-1),
                Coord(1,1),Coord(1,-1)
            ]
            out = []
            for delta in deltas:
                temp = c+delta
                while (temp.isValid() and self.getSquare(temp).team != p.team):
                    if(self.getSquare(temp).team == enemyTeam):
                        out.append(temp)
                        break
                    out.append(temp)
                    temp = temp+delta
            return out
        elif p.name == "queen":
            deltas = [
                Coord(-1,0),Coord(1,0),
                Coord(0,1),Coord(0,-1),
                Coord(-1,1),Coord(-1,-1),
                Coord(1,1),Coord(1,-1)
            ]
            out = []
            for delta in deltas:
                temp = c+delta
                while (temp.isValid() and self.getSquare(temp).team != p.team):
                    if(self.getSquare(temp).team == enemyTeam):
                        out.append(temp)
                        break
                    out.append(temp)
                    temp = temp+delta
            return out

    def getSquare(self, c:Coord):
        if(c.isValid() == False):
            return -1
        return self.board[c.y][c.x]
    
    def setSquare(self, c:Coord, p:Piece):
        if(c.isValid() == False):
            return -1
        self.board[c.y][c.x] = p

