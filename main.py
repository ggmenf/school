from menu.key_0 import good_by
from menu.key_1 import key_1
from menu.key_2 import key_2
from menu.key_3 import key_3
from menu.key_4 import create_new_timetable
from menu.key_5 import key_5
from menu.key_6 import key_6

menu = {
    1: 'Посмотреть расписание',
    2: 'Посмотреть успеваемость',
    3: 'Ввести оценки',
    4: 'Создать новое расписание',
    5: 'Редактировать расписание',
    6: 'Удалить расписание',
    0: 'Выйти',
}


def print_menu(any_menu):
    for k, v in any_menu.items():
        print(f'{k}. {v}')


def run_from_menu(any_menu):
    option: int = int(input('Введи цифру из пункта меню: '))
    print(f'выбрано: \"{option}. {any_menu[option]}\"')
    if option == 0:
        good_by()
    if option == 1:
        key_1()
    if option == 2:
        key_2()
    if option == 3:
        key_3()
    if option == 4:
        create_new_timetable()
    if option == 5:
        key_5()
    if option == 6:
        key_6()


if __name__ == '__main__':
    print()
    print_menu(menu)
    print()
    while True:
        run_from_menu(menu)
        print()
