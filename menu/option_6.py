import os

from utils import print_timetable_names


def remove_timetable():
    if print_timetable_names():
        timetable_name = input('Введите имя расписания: ')
        file_name = f'{timetable_name}.bin'
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f'Расписание {timetable_name} удалено.')
        else:
            print(f'Ошибка: файл {file_name} не найден')
