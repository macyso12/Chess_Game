from game import Game
from coord import Coord
from piece import Piece
from CLI import printGame,printValidMoves,printPossibleMoves

    
if __name__ == "__main__":
    g = Game()
    printGame(g)
    moveList = [
        [Coord(5,6), Coord(5,4)],
        [Coord(4,1), Coord(4,3)],
        [Coord(6,6), Coord(6,4)],
        [Coord(3,0), Coord(7,4)]
    ]
    for move in moveList:
        print(g.makeMove(move[0], move[1]))
        printGame(g)
        if(g.isCheckMate(0)):
            print("White wins by getting checkmated!")
            break
        if(g.isCheckMate(1)):
            print("Black wins by getting checkmated!")
            break
    for move in g.log:
        print(f"{move[0]} -> {move[1]}")