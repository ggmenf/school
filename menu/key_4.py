import pickle

from data import days


def create_new_table():
    chest = {}

    for day in days:
        lessons = []
        print(f'----> {day}:')
        count_lessons = int(input('Введите количесво уроков: '))
        for i in range(count_lessons):
            lesson = input(f'Введите урок {i + 1}: ')
            lessons.append(lesson)
        chest[day] = lessons
        print()

    file_name = input('Сохранить расписание как: ')
    with open(f'{file_name}.txt', 'wb') as f:
        pickle.dump(chest, f)

    with open(f'{file_name}.txt', 'rb') as f:
        chest = pickle.load(f)

    print()
    print(chest)
