"""
The code implements a simple Tic-Tac-Toe game where the player competes against the computer.
"""
from termcolor import colored



board = list(range(1, 10))
winners = ((0, 1, 2), (3, 4, 5), (6, 7, 7), (0, 3, 6), (1, 4, 7), (2, 5 ,8), (0, 4, 8), (2, 4, 6))
moves = ((1, 7, 3, 9), (5,), (2, 4, 6, 8))

def print_board():
    j = 1 
    for i in board:
        end = ' '
        if j % 3 == 0:
            end = '\n\n'
        if i == 'x':
            print(colored(f'[{i}]','red'), end = end)
        elif i == 'o':
            print(colored(f'[{i}]','blue'), end = end)
        else:
            print(f'[{i}]', end = end)
        j += 1
        

def make_move(brd, plyr, mve, undo = False):
    if can_move(brd, mve):
        brd[mve - 1] = plyr
        win = is_winner(brd, plyr)
        if undo:
            brd[mve-1] = mve
        return True, win 
    return False, False
        

def can_move(brd, mve):
    if mve in range(1, 10) and isinstance(brd[mve - 1], int):
        return True
    return False
        
        
def is_winner(brd, plyr):
    win = True
    for tup in winners:
        win = True
        for j in tup:
            if brd[j] != plyr:
                win = False
                break
        if win:
            break
    return win

def has_empty_space():
    return board.count('x') + board.count('o') != 9


def computer_move():
    mv = -1 
    for i in range(1, 10):
        if make_move(board, Computer, i, True)[1]:
            mv = i
            break
    if mv == -1 :
        for j in range(1, 10):
            if make_move(board, Player, j, True)[1]:
                mv = j
                break
    if mv == -1:
        for tup in moves:
            for m in tup:
                if mv == -1 and can_move(board, m):
                    mv = m 
                    break
    return make_move(board, Computer, mv)

            
Player, Computer = 'x' , 'o'
print('Player: X\nComputer: O \n')
while has_empty_space():
    print(print_board())
    move = int(input('Choose your move(1-9) : \n'))
    moved, won = make_move(board, Player, move)
    
    if not moved:
        print(colored('---------------------*---------------------', 'green'))      
        print('Invalid Number, Try Again!')
        print(colored('---------------------*---------------------', 'green'))      
        continue
    
    if won:
        print(colored('---------------------*---------------------', 'green'))      
        print(colored('YOU WON!', 'green'))
        print(colored('---------------------*---------------------', 'green'))      
        break
    
    elif computer_move()[1]:
        print(colored('---------------------*---------------------', 'green'))      
        print(colored('YOU WON!', 'yellow'))
        print(colored('---------------------*---------------------', 'green'))      


print(colored('---------------------*---------------------', 'green'))      
print_board()
print(colored('---------------------*---------------------', 'green'))      
