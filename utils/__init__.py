import pickle

from glob import glob


def get_list_of_timetable_names():
    list_of_saved_timetables = []
    for timetable_name in glob("*.bin"):
        list_of_saved_timetables.append(timetable_name)
    return list_of_saved_timetables


def print_list_of_timetable_names():
    print('Список расписаний:')
    for timetable_name in get_list_of_timetable_names():
        print(f' - {timetable_name.split(".")[0]}')
    print()


def get_timetable_from_file(file_name):
    timetable = {}
    try:
        with open(f"{file_name}.bin", 'rb') as f:
            timetable = pickle.load(f)
    except FileNotFoundError as e:
        print(f'ERROR: расписания \"{file_name}\" нет в списке.')
    return timetable


def write_timetable_to_file(timetable, file_name):
    with open(f'{file_name}.bin', 'wb') as f:
        pickle.dump(timetable, f)
