from data import days

for day in days:
    lessons = []
    print(day)
    count_lessons = int(input('введиет количесво уроков: '))

    for i in range(count_lessons):
        lessons.append(input(f'введите урок {i + 1}: '))
        rating = int(input('введите ожидаемую оценку: '))

    print(lessons)
