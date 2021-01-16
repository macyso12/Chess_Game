class Piece:
    def __init__(self, pieceType:str, team:int, id:int):
        self.type = pieceType #type
        self.team = team #0 if white, 1 if black
        self.id = id     #Individual piece, if placeholder then 0, if piece, 1->32
    
    def toStr(self):
        if self.id == 0:
            return {"type":"null"}
        return {"type":self.type, "team":self.team, "id":self.id}
        
class Game:
    def __init__(self):
        self.board = [[Piece("NULL", "NULL", 0) for x in range(8)] for y in range(8)]
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

if __name__ == '__main__':
    g = Game()
    g.debugPrint()
    print(g.board[0][3].toStr())