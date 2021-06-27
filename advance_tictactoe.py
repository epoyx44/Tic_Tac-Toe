#kulang scoring
import random
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

new_board = board[:]

tic = ["x","o"]
ran1,ran2 = random.sample(tic,k=2)

def checkdraw(boards):
    if '-' not in boards:
        print('DRAW!!')




def displayboard(boards):
    print(boards[0] + "|" + boards[1] + "|" +boards[2])
    print(boards[3] + "|" + boards[4] + "|" +boards[5])
    print(boards[6] + "|" + boards[7] + "|" + boards[8])

def player1(boards):
    on = True
    print("player 1 you are {}".format(ran1))
    while on:
        try:
            playerone = (input("where to put:"))
            num = int(playerone) - 1

            if num >= 9:
                print('you exceeded only 1-9')
                continue
            elif boards[num] == '-':
                boards[num] = ran1

            elif boards[num] != '-':
                print('Its already played!')
                continue
        except ValueError:
            print('please print numbers only')
            continue
        on = False
    displayboard(boards)


def player2(boards):
    on = True
    print('playertwo you are {}'.format(ran2))
    while on:
        try:
            playertwo = input('player two where to put:')
            num = int(playertwo) - 1
            if num >= 9:
                print('you are {} and be sure number is 1-9 only'.format(ran2))
                continue
            elif boards[num] == '-':
                boards[num] = ran2
            elif boards[num] != '-':
                print('Its already played!')
                continue
            else:
                print('Its already played!')
                continue
        except ValueError:
            print('please print numbers only')
            continue
        on = False
    displayboard(boards)

def checkwin(boards):
    if boards[0] == boards[3] == boards[6] != '-':
        if boards[0] == ran1:
            print('The winner is {}'.format(ran1))
        else:
            print('The winner is {}'.format(ran2))
        return True
    elif boards[0] == boards[4] == boards[8] != '-':
        if boards[0] == ran1:
            print('The winner is {}'.format(ran1))
        else:
            print('The winner is {}'.format(ran2))
        return True
    elif boards[0] == boards[1] == boards[2] != '-':
        if boards[0] == ran1:
            print('The winner is {}'.format(ran1))
        else:
            print('The winner is {}'.format(ran2))
        return True
    elif boards[2] == boards[5] == boards[8] != '-':
        if boards[2] == ran1:
            print('The winner is {}'.format(ran1))
        else:
            print('The winner is {}'.format(ran2))
        return True
    elif boards[6] == boards[7] == boards[8] != '-':
        if boards[6] == ran1:
            print('The winner is {}'.format(ran1))
        else:
            print('The winner is {}'.format(ran2))
        return True
    elif boards[3] == boards[4] == boards[5] != '-':
        if boards[3] == ran1:
            print('The winner is {}'.format(ran1))
        else:
            print('The winner is {}'.format(ran2))
        return True
    elif boards[1] == boards[4] == boards[7] != '-':
        if boards[1] == ran1:
            print('The winner is {}'.format(ran1))
        else:
            print('The winner is {}'.format(ran2))
        return True
    elif boards[6] == boards[4] == boards[2] != '-':
        if boards[6] == ran1:
            print('The winner is {}'.format(ran1))
        else:
            print('The winner is {}'.format(ran2))
        return True
    else:
        pass
    return False

def main():

    turns = 0 # variable to let me know if the board is full
    while True:
        player1(board)
        if checkwin(board):
            break
        turns += 1
        if turns == 5:
            checkdraw(board)
            break
        player2(board)
        if checkwin(board):
            break
while True:
    main()
    a = input('y or n: ')
    if a == 'y':
        board = new_board
        continue
    elif a == 'n':
        break

