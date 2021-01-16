from game import Game
from coord import Coord
from piece import Piece
from CLI import printGame,printValidMoves,printPossibleMoves

    
if __name__ == "__main__":
    g = Game()
    c = Coord(5,6)
    g.setSquare(c, Piece("queen", 1, 3, 1))
    g.setSquare(Coord(7,4), Piece("bishop", 1, 3, 1))
    printGame(g)
    printPossibleMoves(g, c)
    # print(g.isCheckMate(1))
    print(g.kingInCheck(0))
    print(g.isCheckMate(0))
    # print(g.getValidMoves(Coord(0,6)))