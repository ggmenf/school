import pickle

from glob import glob


def get_timetable_names():
    timetable_names = []
    for timetable_name in glob("*.bin"):
        timetable_names.append(timetable_name)
    return timetable_names


def print_timetable_names():
    timetable_names = get_timetable_names()
    if timetable_names:
        print('Список расписаний:')
        for timetable_name in timetable_names:
            print(f' - {timetable_name.split(".")[0]}')
        print()
        return True
    else:
        print('Нет сохранённых расписаний')
        return False


def get_timetable(file_name):
    timetable = {}
    try:
        with open(f"{file_name}.bin", 'rb') as f:
            timetable = pickle.load(f)
    except FileNotFoundError as e:
        print(f'ERROR: расписания \"{file_name}\" нет в списке.')
    return timetable


def write_timetable(timetable, file_name):
    with open(f'{file_name}.bin', 'wb') as f:
        pickle.dump(timetable, f)
