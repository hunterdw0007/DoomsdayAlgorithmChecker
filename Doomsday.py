
import random
import time
import datetime
from datetime import datetime
import calendar

# https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates

def time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return datetime.fromtimestamp(ptime)

def random_date(start, end, prop):
    return time_prop(start, end, '%m/%d/%Y', prop)

correct = 0
total = 0
play = True
while play:
    date = random_date('1/1/1900', '12/31/2099', random.random())

    print()
    print(date.strftime('%m/%d/%Y'))
    print('\nEnter Weekday: ')
    weekday_guess = input()

    if(weekday_guess.upper() == 'EXIT'):
        play = False
    elif(weekday_guess == calendar.day_name[date.weekday()]):
        print('CORRECT')
        correct += 1
        total += 1
    else:
        print('INCORRECT - it is a ' + calendar.day_name[date.weekday()])
        total += 1

    
    average = correct/total * 100 if total != 0 else 0
    print(f'\nScore is: {correct}/{total}')
    print(f'\nAverage is: {average:.2f}%')
