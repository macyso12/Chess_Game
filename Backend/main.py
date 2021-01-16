from game import Game
from coord import Coord
from piece import Piece
from CLI import printGame,printValidMoves,printPossibleMoves

    
if __name__ == "__main__":
    g = Game()
    printGame(g)
    c = Coord(6,6)
    g.setSquare(c, Piece("knight", 0))
    g.setSquare(Coord(5,6), Piece())
    g.setSquare(Coord(3,5), Piece("pawn", 1, 3, 0))
    g.setSquare(Coord(7,4), Piece("bishop", 1, 3, 1))
    # g.setSquare(c, Piece("pawn", 0, 3, 0))
    # g.movePiece(c, c+Coord(0,-1))
    # printGame(g)
    print([str(x) for x in g.getValidMoves(c)])
    printValidMoves(g, c)
    