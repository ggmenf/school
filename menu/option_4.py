import utils
from data import days


def create_new_timetable():
    timetable = {}

    for day in days:
        lessons = []
        print(f'----> {day}:')
        while True:
            try:
                count_lessons = int(input('Введите количесво уроков: '))
                break
            except:
                print('Ошибка: необходимо ввести число')
        for i in range(count_lessons):
            lesson = input(f'Введите урок {i + 1}: ')
            lessons.append(lesson)
        timetable[day] = lessons
        print()

    file_name = input('Сохранить расписание как: ')

    utils.write_timetable(timetable, file_name)

    print('Готово')
