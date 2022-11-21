from data import school_objects, days, lesson_time
from timetable import timetable

for i in range(len(timetable)):
    print(f'{days[i]}:')
    for j in range(len(timetable[i])):
        if timetable[i][j] == ['выходной']:
            print(f'\t{timetable[i][j]}')
        else:
            print(f'\t{lesson_time[j]}:  {timetable[i][j]}')
    print()
