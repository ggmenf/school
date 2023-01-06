from utils import (
    get_timetable_from_file,
    print_list_of_timetable_names
)


def print_timetable():
    print_list_of_timetable_names()

    timetable_name = input('Введите имя расписания: ')

    for day, items in get_timetable_from_file(timetable_name).items():
        print()
        print(f'{day}:')
        i = 1
        for item in items:
            print(f'  {i}. {item}')
            i += 1
