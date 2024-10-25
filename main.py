import random
import datetime

"""
very raw version -- not done and not totally functional right yet!!
"""

def init_set():
    print('=====================================================\n\t\t\tCSC 290 Chess Bot V.01 by Chaira and Glory\t\t\t\n=====================================================')
    print('Time:', datetime.datetime.now())
    comp = ''
    while(comp not in ['w', 'b', 'white', 'black', 'wh', 'bl']):
        comp = input('Computer Player? (w=white/b=black): ')
    # starting_pos = input('Starting FEN position? (hit ENTER for standard starting position): ')
    if 'w' in comp:
        print('You are playing as BLACK. The computer will start first.\n')
    elif 'b' in comp:
        print('You are playing as WHITE. Please begin the first move.\n')
    print('\n')
    return comp


def init_board():
    # Black pieces are lower case, white pieces are upper case.
    return [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]
    

def update_board(board):
    print('    a   b   c   d   e   f   g   h')
    for row in range(8):
        print(f'{8 - row} |', end=' ')
        for col in range(8):
            print(f'{board[row][col]} |', end=' ')
        print(f'{8 - row}')
        if row < 7:
            print('  ---------------------------------')
    print('    a   b   c   d   e   f   g   h\n')
    
def move_piece(board, move_choice, colour):
    src = move_choice[:2]
    dest = move_choice[2:]

    srcc = ord(src[0]) - ord('a')
    srcr = 8-int(src[1])

    destc = ord(dest[0]) - ord('a')
    destr = 8-int(dest[1])

    # print('debug: ', board[srcr][srcc]) 

    # board[destr][destc] = board[srcr][srcc]
    board[destr][destc] = 'P'
    board[srcr][srcc] = ' '

    print(colour, ' moved from', src, ' to', dest, '\n')
    update_board(board)



def move(comp, board):
    if 'w' in comp:
        move_piece(board, 'e2e4', 'w') 
    elif 'b' in comp:
        move_choice = ''
        while not len(move_choice == 4):
            move_choice = input('Enter move: (ie f2f4) ')
        move_piece(board, move_choice, 'b')

def main():
    comp = init_set()
    board = init_board()

    update_board(board) # initial board

    checkmate = False

    while(not checkmate):
        move(comp, board)
        checkmate = True # just for now so it doesn't run forever.

if __name__ == '__main__':
    main()