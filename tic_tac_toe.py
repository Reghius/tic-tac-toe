
def print_canvas(canvas):
    for i in range(len(canvas)):
        for j in range(len(canvas[i])):
            print(canvas[i][j] + ' ', end='')
        print()
    print()

def get_user_input(tablica, player_sign='X'):
    while True:
        column = input('input x(0-2): ')
        while int(column) > 2 or int(column) < 0:
            print('please input number between 0 and 2')
            column = input('input x(0-2): ')

        row = input('input y(0-2): ')
        while int(row) > 2 or int(row) < 0:
            print('please input number between 0 and 2')
            row = input('input y(0-2): ')

        if tablica[int(row)][int(column)] == '_':
            tablica[int(row)][int(column)] = player_sign
            break
        else:
            print('Position occupied; input correct position.')

    return tablica

def check_game_logic(tablica):
    if tablica[0] == ['X', 'X', 'X'] or tablica[1] == ['X', 'X', 'X'] or tablica[2] == ['X', 'X', 'X']:
        return 'X'
    if tablica[0] == ['O', 'O', 'O'] or tablica[1] == ['O', 'O', 'O'] or tablica[2] == ['O', 'O', 'O']:
        return 'O'
    for i in range(3):
        if tablica[0][i] == 'X' and tablica[1][i] == 'X' and tablica[2][i] == 'X':
            return 'X'
        if tablica[0][i] == 'O' and tablica[1][i] == 'O' and tablica[2][i] == 'O':
            return 'O'
    if tablica[0][0] == 'X' and tablica[1][1] == 'X' and tablica[2][2] == 'X':
        return 'X'
    if tablica[2][0] == 'X' and tablica[1][1] == 'X' and tablica[0][2] == 'X':
        return 'X'
    if tablica[0][0] == 'O' and tablica[1][1] == 'O' and tablica[2][2] == 'O':
        return 'O'
    if tablica[2][0] == 'O' and tablica[1][1] == 'O' and tablica[0][2] == 'O':
        return 'O'

    return ''

if __name__ == '__main__':
    canvas = [
        ['_','_','_'],
        ['_','_','_'],
        ['_','_','_']
    ]
    current_sign = 'X'

    for i in range(9):
        print_canvas(canvas)
        canvas = get_user_input(canvas, player_sign=current_sign)

        if current_sign == 'X':
            current_sign = 'O'
        else:
            current_sign = 'X'
        
        winner = check_game_logic(canvas)
        if winner == 'X':
            print('X won the game')
            break
        if winner == 'O':
            print('O won the game')
            break
