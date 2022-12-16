from menu.option_0 import good_by
from menu.option_1 import print_timetable
from menu.option_2 import option_2
from menu.option_3 import option_3
from menu.option_4 import create_new_timetable
from menu.option_5 import option_5
from menu.option_6 import option_6

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
        print_timetable()
    if option == 2:
        option_2()
    if option == 3:
        option_3()
    if option == 4:
        create_new_timetable()
    if option == 5:
        option_5()
    if option == 6:
        option_6()


if __name__ == '__main__':
    while True:
        print()
        print_menu(menu)
        print()
        run_from_menu(menu)
        print()
