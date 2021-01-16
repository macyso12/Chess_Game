class Piece:
    def __init__(self, pieceType:str = "null", team:int = -1, id:int = 0):
        self.type = pieceType #type
        self.team = team #0 if white, 1 if black
        self.id = id     #Individual piece, if placeholder then 0, if piece, 1->32
    
    def toStr(self):
        if self.id == 0:
            return {"type":"null"}
        return {"type":self.type, "team":self.team, "id":self.id}

class Game:
    def __init__(self):
        self.board = [[Piece() for x in range(8)] for y in range(8)]
        pieces = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
        for i in range(1,9):
            self.board[0][i-1] = Piece(pieces[i-1], 1, i)
        for i in range(9,17):
            self.board[1][i-9] = Piece("pawn", 1, i)
        for i in range(17,25):
            self.board[6][i-17] = Piece("pawn", 0, i)
        for i in range(25,33):
            self.board[7][i-25] = Piece(pieces[i-25], 0, i)
                
    def debugPrint(self):
        printMap = {
            "queen" :"Q",
            "king"  :"K",
            "pawn"  :"p",
            "rook"  :"R",
            "bishop":"B",
            "knight":"K",
            "null"  :" "
        }
        print("██████████")
        for row in self.board:
            print("█", end="")
            for item in row:
                print(printMap[item.type.lower()], end = "")
            print("█")
        print("██████████")

    def debugPrintMoves(self, x, y):
        printMap = {
            "queen" :"Q",
            "king"  :"K",
            "pawn"  :"p",
            "rook"  :"R",
            "bishop":"B",
            "knight":"K",
            "null"  :" "
        }

        moves = self.getMoves(x,y)
        print("██████████")
        for y in range(len(self.board)):
            print("█", end="")
            for x in range(len(self.board[y])):
                if((x,y) not in moves):
                    print(printMap[self.board[y][x].type.lower()], end = "")
                else:
                    print("#",end="")
            print("█")
        print("██████████")

    def coordInBoard(self, x, y):
        return (0<=x and x<=7 and 0<=y and y<=7)

    def getMoves(self, x, y):
        p = self.board[y][x]
        enemy = 0 if p.team ==1 else 1
        if p.type == "knight":
            deltas = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2, -1), (-2, 1), (-1, 2)]
            out = []
            for delta in deltas:
                newX = x+delta[0]
                newY = y+delta[1]
                if self.coordInBoard(newX, newY):
                    out.append((newX, newY))
            return out
        elif p.type == "queen":
            out = []
            dirs = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,-1), (-1, 1)]
            for direction in dirs:
                dX = x
                dY = y
                while True:
                    dX+=direction[0]
                    dY+=direction[1]
                    if(self.coordInBoard(dX, dY) == False):
                        break
                    if(self.board[dY][dX].team == self.board[y][x].team):
                        break
                    if(self.board[dY][dX].team == enemy):
                        out.append((dX,dY))
                        break
                    out.append((dX,dY))
            return out
        elif p.type == "rook":
            out = []
            dirs = [(0,1), (1,0), (0,-1), (-1,0)]
            for direction in dirs:
                dX = x
                dY = y
                while True:
                    dX+=direction[0]
                    dY+=direction[1]
                    if(self.coordInBoard(dX, dY) == False):
                        break
                    if(self.board[dY][dX].team == self.board[y][x].team):
                        break
                    if(self.board[dY][dX].team == enemy):
                        out.append((dX,dY))
                        break
                    out.append((dX,dY))
            return out

        return "error"
            


if __name__ == '__main__':
    g = Game()
    coord = (3, 4)
    g.board[1][3] = Piece()
    g.board[3][4] = Piece("knight", 1, 12)
    g.board[0][3] = Piece()
    g.debugPrint()
    print(g.board[coord[1]][coord[0]].toStr())
    print(g.getMoves(coord[0], coord[1]))
    g.debugPrintMoves(coord[0], coord[1])