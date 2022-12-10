# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока 
# делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты 
# оппонента достаются сделавшему последний ход. Сколько конфет 
# нужно взять первому игроку, чтобы забрать все конфеты у 
# своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# Доп. условия не выполнены :(

from random import randint

def give_int(name) -> int:
    '''
    Функция ввода числа
    '''
    while True:
        try:
            low = 1
            high = 28
            num = int(input(f'Сколько конфет Вы берете {name}: ')) 
            if num < low:
                print(f'Вам нужно взять хотя-бы одну конфету {name}.')
                continue   
            if num > high:
                print(f'Вы не можете взять так много конфет {name}. Попробуйте по меньше.')
                continue
            return num
        except ValueError:
            print('Вы ввели не число. Введите число.')

gamer_1 = input("Введите имя первого игрока: ")
gamer_2 = input("Введите имя второго игрока: ")
amount = 2021
flag = randint(0,2)

if flag:
    print(f'Первым будет ходить {gamer_1}')
else:
    print(f'Первым будет ходить {gamer_2}')
    
def text_print(name, counter, amount):
    '''
    Функция печати
    '''
    print(f'Конфет осталось: {amount} шт. Всего конфет у {name}: {counter} шт.')

count_1 = 0 
count_2 = 0

while amount > 28:
    if flag:
        number = give_int(gamer_1)
        count_1 += number
        amount -= number
        flag = False
        text_print(gamer_1, count_1, amount)
    else:
        number = give_int(gamer_2)
        count_2 += number
        amount -= number
        flag = True
        text_print(gamer_2, count_2, amount)

if flag:
    print(f'Поздравляем {gamer_1}! Вы выиграли. Теперь все кофеты Ваши.')
else:
    print(f'Поздравляем {gamer_2}! Вы выиграли. Теперь все кофеты Ваши.')
