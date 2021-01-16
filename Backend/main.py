from game import Game
from coord import Coord
from piece import Piece
from colorama import Fore, Back, Style


def printGame(g:Game):    
    b = g.board
    print(Style.BRIGHT,end="")
    print(Fore.RED+"     Black  "+Fore.RESET)
    print("  "+"▄"*10)
    for y in range(len(b)):
        print(f"{y} █", end="")
        for x in range(len(b[y])):
            print(Back.LIGHTBLACK_EX if (x+y)%2 == 1 else Back.BLACK, end="")
            if(b[y][x].team == 1):
                print(Fore.RED,end="")
            elif(b[y][x].team == 0):
                print(Fore.BLUE,end="")
            print((b[y][x].name.upper()[0] if b[y][x].name != "Knight" else "H") if b[y][x].team != -1 else " ", end ="")
            print(Back.RESET+Fore.RESET,end = "")
        print("█")
    print("  "+"▀"*10)
    print(Fore.BLUE+"     White  "+Fore.RESET)
    print(Style.RESET_ALL,end="")



if __name__ == "__main__":
    g = Game()
    printGame(g)