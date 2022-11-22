import pickle

from data import days

chest = {}

for day in days:
    lessons = []
    print(day)
    count_lessons = int(input('введиет количесво уроков: '))

    for i in range(count_lessons):
        lesson = input(f'введите урок {i + 1}: ')
        lessons.append(lesson)

    chest[day] = lessons

    print(f'---------------------> {chest}')

file_name = input('сохранить расписание как: ')

with open(f'{file_name}.txt', 'wb') as f:
    pickle.dump(chest, f)

with open(f'{file_name}.txt', 'rb') as f:
    chest = pickle.load(f)

print(chest)
