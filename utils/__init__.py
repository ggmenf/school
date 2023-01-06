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
