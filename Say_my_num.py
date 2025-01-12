'''Игра, в которой человек или компьютер угадывает числа!
функции:
    1) Выводится количество попыток, скольоко понадобилось попыток для угадывания числа;
    2) В конце игры производится запорос на новую игру;
    3) Два режима игры;
'''

import random


def menu():
    'Показывает меню игры и возвращает выбор пользователя'
    print('Выберете режим игры:')
    print('1) Компьютер угадывает ваше число', '2) Вы угадываете число, которое компьютер загадал ', sep='\n')
    return input()


def start_settings() -> int:
    'Задает начало игры, запрашивает диапазаон чисел'
    print('Введите диапазон чисел, с которым хотите играть')

    print('Начало: ', end='')
    a = input_num()
    print('Конец: ', end='')
    b = input_num()
    return a, b


def input_num() -> int:
    'Обеспечивает валидность вводимых данных'
    a = input()
    while True:
        if a.isdigit():
            break
        else:
            print('Проверьте правильность ввода данных, это должны быть целые числа!')
    return int(a)


while True:
    Counter = 0  # Переменная счетчика

    user_choice = menu()
    if user_choice == '1':
        N = int(input('Введите диапозон, среди которого есть ваше число от 1 до: '))  # Входящее число
        Nums = [i for i in range(1, N + 1)]  # Заполняем список числами от 1 до N включительно
        print(Nums)
        N_half = Nums[len(Nums) // 2]  # Делим список пополоам, что бы задать вопрос и отсеять половину ненужных ответов

        while len(Nums) > 1:
            print(f'В какую сторону отличается ваше загаданное число от {N_half}? (>, <, =)')  # Вопрос равенства
            check_sign = input()  # Переменная, содержащая знак отличия
            Counter += 1  # Счетчик попыток

            if check_sign == '>':  # Если больше, то отсекаем меньшие значения в списке ( половину списка)
                Nums = Nums[len(Nums) // 2:]
                N_half = N_half = Nums[len(Nums) // 2]
            elif check_sign == '<':  # Если меньше, то отсекаем бОльшие значения в списке ( половину списка)
                Nums = Nums[:len(Nums) // 2]
                N_half = N_half = Nums[len(Nums) // 2]
            else:
                print(f'Ура, я отгадал число, загаданное вами число {N_half}!')  # Равенство - победа, выход из цикла
                break
    elif user_choice == '2':
        a, b = start_settings()
        RNum = int(random.randint(a, b))  # Случайное число из диапазаона a,b

        print('Попробуйте угадать число!')
        while True:  # Цикл тела игры при 2 режиме
            U_Num = input_num()
            Counter += 1

            if U_Num == RNum:
                print('Вы отгадали число, поздравляю!')
                break
            elif U_Num < RNum:
                print('Загаданное число больше')
            elif U_Num > RNum:
                print('Загаданное число меньше')

    print(
        f'Количество попыток: {Counter}') if user_choice or Counter > 0 else None  # Если выбор не валиден, то не показываем счетчик

    print('Хотите начать новую игру? 1/0')  # Блок запроса на новую игру
    again = input()
    if again == '0':
        print('Спасибо за игру!')
        break
