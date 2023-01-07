import utils
from .option_1 import print_timetable

from data import days


def edit_timetable():
    if utils.print_timetable_names():
        timetable = {}
        while not timetable:
            timetable_name = input('Введите имя расписания списка выше: ')
            timetable = utils.get_timetable(timetable_name)
        while True:
            try:
                print('0 - Вывести расписание за неделю')
                print('1 - Вывести расписание за один день')
                option: int = int(input('Сделайте выбор: '))
                break
            except:
                print('Ввдетите число 0, либо 1')
        if option == 0:
            print_timetable()
        if option == 1:
            pass
        while True:
            day = input('Введите день: ').lower().title()
            if day in days:
                print()
                print(timetable[day])
                break
            else:
                print(f'Ошибка: неправильно введён день недели \"{day}\"')
                print(f'Выберите день из списка: {days}')
