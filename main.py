field = [' '] * 9
win = [[0, 1, 2], [3, 4, 5], [6, 7, 8],[0, 3, 6], [1, 4, 7], [2, 5, 8],[0, 4, 8], [2, 4, 6]]
current_player = 'X'

def display_field():
    print(field[0] + '|' + field[1] + '|' + field[2])
    print('-+-+-')
    print(field[3] + '|' + field[4] + '|' + field[5])
    print('-+-+-')
    print(field[6] + '|' + field[7] + '|' + field[8])

def move():
    global current_player
    position = int(input("Выберите позицию для хода (от 1 до 9): ")) - 1
    if field[position] == ' ':
        field[position] = current_player
        display_field()
        check_winner()
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
    else:
        print("Недопустимый ход. Попробуйте еще раз.")
        move()

def check_winner():
    for combination in win:
        if field[combination[0]] == field[combination[1]] == field[combination[2]] != ' ':
            print("Игрок", current_player, "победил")
            exit()
    if ' ' not in field:
        print("Ничья")
        exit()

display_field()
while True:
    move()