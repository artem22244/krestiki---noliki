board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# количество строчек по горизантали
n = 3


def game_board():
    print('_' * 4 * n)
    for i in range(n):
        print((' ' * n + '|') * 3)
        print('', board[i * 3], '|', board[i * 3 + 1], '|', board[i * 3 + 2], '|')
        print(('_' * n + '|') * 3)


def game_step(index,  char):
    if (index > 9 or index < 1 or board[index-1] in ('X', 'O')):
        return False
    board[index - 1] = char
    return True



def check_win():
    win = False
    win_combination = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))

    for pos in win_combination:
        if (board[pos[0]]== board[pos[1]] and board[pos[1]]== board[pos[2]]):
            win = board[pos[0]]


    return win


def game_start():
    # текущий игрок
    current_player = 'X'
    # количество ходов
    step = 1
    game_board()
    while (step < 10) and (check_win() == False):
        index = input('ходит игрок ' + current_player + ' (если захотите остновить игру нажмите на - 0).---')

        if (index == '0'):
            break
        if (game_step(int(index), current_player)):
            print('вы совершили возможный ход')
            if (current_player == 'X'):
                current_player = 'O'
            else:
                current_player = 'X'

            game_board()
            step += 1

        else:
            print('невозможный ход, повторите попытку')

    if (step == 10):
        print('ничья')
    print('выиграл' + check_win())



print('Начинается игра')
game_start()
