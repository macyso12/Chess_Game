from game import Game
from coord import Coord
from piece import Piece
from CLI import printGame,printValidMoves,printPossibleMoves

    
if __name__ == "__main__":
    g = Game()
    c = Coord(7,6)
    g.setSquare(Coord(7,4), Piece("bishop", 1, 3, 1))
    g.setSquare(Coord(5,6), Piece("queen", 1, 3, 1))
    g.setSquare(Coord(6,6), Piece())
    g.setSquare(Coord(5,7), Piece("pawn", 0, 3, 0))
    # g.movePiece(c, c+Coord(0,-1))
    printGame(g)
    # printGame(g)
    # print([str(x) for x in g.getValidMoves(c)])

    # printValidMoves(g, Coord(5,7))
    # print("valids: ",g.getValidMoves(Coord(6,7)))
    printPossibleMoves(g, Coord(5,6))
    # print(g.isCheckMate(1))
    print(g.kingInCheck(1))
    print(g.kingInCheck(0))