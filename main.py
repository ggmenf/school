from data import school_objects, days, lesson_time
from timetable import timetable

for i in range(len(timetable)):
    print(f'{days[i]}:')
    for j in range(len(timetable[i])):
        print(f'\t{lesson_time[j]}:  {timetable[i][j]}')
    print()
