import os

from utils import print_list_of_saved_timetables


def remove_timetable():
    print_list_of_saved_timetables()
    timetable_name = input('Введите имя расписания: ')
    os.remove(f'{timetable_name}.txt')
    print(f'Расписание {timetable_name} удалено.')
