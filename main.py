from data import school_objects, days, lesson_time

timetable = [

    [
        school_objects[9],
        school_objects[10],
        school_objects[0],
        school_objects[7],
        school_objects[8],
    ],
    [
        school_objects[1],
        school_objects[4],
        school_objects[10],
        school_objects[3],
        school_objects[11],
        school_objects[0],
    ],
    [
        school_objects[2],
        school_objects[2],
        school_objects[9],
        school_objects[5],
        school_objects[0],
        school_objects[3],
    ],
    [
        school_objects[4],
        school_objects[11],
        school_objects[6],
        school_objects[0],
        school_objects[12],
        school_objects[5],
    ],
    [
        school_objects[9],
        school_objects[4],
        school_objects[5],
        school_objects[11],
        school_objects[6],
        school_objects[0],
    ],
    [
        ['выходной'],
    ],
    [
        ['выходной'],
    ],
]

# range(100)

for i in range(len(timetable)):
    print(f'{days[i]}:')
    for j in range(len(timetable[i])):
        print(f'\t{lesson_time[j]}:  {timetable[i][j]}')
    print()
