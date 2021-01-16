from game import Game
from coord import Coord
from piece import Piece
from CLI import printGame,printValidMoves,printPossibleMoves

SCHOLARS_MATE = [
    [Coord(5,6), Coord(5,4)],
    [Coord(4,1), Coord(4,3)],
    [Coord(6,6), Coord(6,4)],
    [Coord(3,0), Coord(7,4)]
]

QUEENING_TEST = [
    [Coord(4,6), Coord(4,4)],
    [Coord(3,1), Coord(3,3)],
    [Coord(4,4), Coord(3,3)],
    [Coord(4,1), Coord(4,2)],
    [Coord(3,3), Coord(4,2)],
    [Coord(3,0), Coord(3,1)],
    [Coord(4,2), Coord(3,1)],
    [Coord(6,0), Coord(5,2)], #invalid knight move
    [Coord(4,0), Coord(3,0)],
    [Coord(3,1), Coord(2,0)]
]


if __name__ == "__main__":
    g = Game()
    printGame(g)

    for move in QUEENING_TEST:
        if(g.makeMove(move[0], move[1])):
            print("Able to make move")
        else:
            print("Unable to make move")
        printGame(g)
        if(g.isCheckMate(0)):
            print("White wins by getting checkmated!")
            break
        if(g.isCheckMate(1)):
            print("Black wins by getting checkmated!")
            break
        print("Black in check:",g.kingInCheck(1))
        print("Score:",g.getScore())
    for move in g.log:
        print(f"{move[0]} -> {move[1]}")