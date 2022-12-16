import pickle

from glob import glob


def get_list_of_saved_timetables():
    list_of_saved_timetables = []
    for timetable_name in glob("*.txt"):
        list_of_saved_timetables.append(timetable_name)
    return list_of_saved_timetables


def get_timetable_from_file(timetable_name):
    timetable = {}
    try:
        with open(f"{timetable_name}.txt", 'rb') as f:
            timetable = pickle.load(f)
    except FileNotFoundError as e:
        print(f'ERROR: расписания \"{timetable_name}\" нет в списке.')
    return timetable


def print_timetable():
    print('Список расписаний:')
    for i in get_list_of_saved_timetables():
        print(f'- {i.split(".")[0]}')
    print()

    timetable_name = input('Введите имя сохранённого расписания: ')

    for day, items in get_timetable_from_file(timetable_name).items():
        print()
        print(f'{day}:')
        i = 1
        for item in items:
            print(f'  {i}. {item}')
            i += 1
