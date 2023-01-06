from utils import (
    get_timetable_from_file,
    get_list_of_saved_timetables
)


def print_timetable():
    print('Список расписаний:')
    for timetable_name in get_list_of_saved_timetables():
        print(f' - {timetable_name.split(".")[0]}')
    print()

    timetable_name = input('Введите имя расписания: ')

    for day, items in get_timetable_from_file(timetable_name).items():
        print()
        print(f'{day}:')
        i = 1
        for item in items:
            print(f'  {i}. {item}')
            i += 1
