board = [['|__']*3 for r in range(3)]


def fun_board(b): 
    print('y')
    for r, board in enumerate(b):
        print(r, *board)
    print('   0    1   2   x')



def fun_player(b):
    while True:
        coord = input('введите два числа через пробел:').split()
        if len(coord) != 2:
            print('неправильный ввод')
            continue
        if not (coord[0].isdigit() and coord[1].isdigit()):
            print('неправильный ввод')
            continue
        x, y = map(int, coord)
        if (x < 0 or y < 0 or x > 2 or y > 2):
            print('неправильное число')
            continue
        if b[y][x] != '|__':
            print('этот ход был, переходите')
            continue
        break
    return x, y


def win(b, player):
    def win_hod(h1, h2, h3, player):
        if player == h1 == h2 == h3:
            return True
        else:
            return False
    for r in range(3):
        if win_hod(b[r][0], b[r][1], b[r][2], player) or \
        win_hod(b[0][r], b[1][r], b[2][r], player) or \
        win_hod(b[0][0], b[1][1], b[2][2], player) or \
        win_hod(b[2][0], b[1][1], b[0][2], player):
            return True
    return False


def game():
    print('Начинаем игру.')
    count = 1
    while True:
        if count % 2 == 1:
            player = '| x'
        else:
            player = '| о'
        print('Ход №:', count, '\nХодит игрок:', player)
        fun_board(board)
        x, y = fun_player(board)
        board[y][x] = player
        count  += 1
        if win(board, player):
            print("Выйграл игрок:" + player)
            fun_board(board)
            break
        if count == 10:
            print('Игра закончена. Ничья')
            fun_board(board)
            break



while True:
    game()
    board = [['|__']*3 for r in range(3)]
    ans = input ("Хотите сыграть еще? Нажмите 1. Если нет, то любую букву")
    if ans != "1":
        break
print("Спасибо за игру!")
    

    