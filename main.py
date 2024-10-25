import random
import datetime

def init():
    print('=====================================================\n\t\t\tCSC 290 Chess Bot V.01 by Chaira and Glory\t\t\t\n=====================================================')
    print('Time:', datetime.datetime.now())
    comp = input('Computer Player? (w=white/b=black): ')
    starting_pos = input('Starting FEN position? (hit ENTER for standard starting position): ')
    print('\n')
    

def update_board():
    # This is our starting board. Black pieces are lower case, white pieces are upper case.
    print('''    a   b   c   d   e   f   g   h
8 | r | n | b | q | k | b | n | r | 8
  ---------------------------------
7 | p | p | p | p | p | p | p | p | 7
  ---------------------------------
6 |   |   |   |   |   |   |   |   | 6
  ---------------------------------
5 |   |   |   |   |   |   |   |   | 5
  ---------------------------------
4 |   |   |   |   |   |   |   |   | 4
  ---------------------------------
3 |   |   |   |   |   |   |   |   | 3
  ---------------------------------
2 | P | P | P | P | P | P | P | P | 2
  ---------------------------------
1 | R | N | B | Q | K | B | N | R | 1
    a   b   c   d   e   f   g   h
''')

def main():
    init()

    checkmate = False

    while(not checkmate):
        update_board()
        checkmate = True

if __name__ == '__main__':
    main()