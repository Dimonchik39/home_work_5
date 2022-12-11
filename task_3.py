# Создайте программу для игры в ""Крестики-нолики"". 
# Для определения победы вам может пригодиться функция
#  filter. Проверяйте победу после каждого хода, 
#  фильтруя столбцы, строки и диагонали по знаку хода

print('----КРЕСТИКИ-НОЛИКИ ДЛЯ 2 ИГРОКОВ----')

board = list(range(1,10))

def board_create(board):
    '''
    Функция создания игрового поля
    '''
    print("-" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 13)
        
def give_input(player_token):
    '''
    Функция ввода числа пользователем
    '''
    valid = False
    while not valid:
        cell_selection = input(f'Выберете ячейку для {player_token}: ')
        try:
            cell_selection = int(cell_selection)
        except:
            print('Введите число от 1 до 9')
            continue
        if cell_selection >= 1 and cell_selection <= 9:
            if(str(board[cell_selection-1]) not in "XO"):
                board[cell_selection-1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print('Введите число от 1 до 9.')

def check_win(board):
    '''
    Функция проверки победителя
    '''
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for i in win_coord:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False
    

def main(board):
    '''
    Функция управления игровым процессом
    '''
    counter = 0
    win = False
    while not win:
        board_create(board)
        if counter % 2 == 0:
            give_input("X")
        else:
            give_input("O")
        counter += 1
        if counter > 4:
            temp = check_win(board)
            temp2 = board_create(board)
            if temp:
                temp2                
                print('Победил', temp)
                win = True
                break
        if counter == 9:
            print("НИЧЬЯ!")
            break
main(board)
