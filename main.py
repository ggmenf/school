from data import school_objects, days, lesson_time
from timetable import timetable

for i in range(len(timetable)):
    print(f'{days[i]}:')
    for j in range(len(timetable[i])):
        obj_key = [key for key in timetable[i][j].keys()]
        if obj_key:
            print(f'\t{lesson_time[j]}:  {obj_key[0]}')
        else:
            print(f'\tвыходной')
    print()
