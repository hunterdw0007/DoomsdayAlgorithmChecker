# Hunter Westerlund
# Github: hunterdw0007
#
# This program gives the user a date randomly chosen between 1/1/1900 and 12/32/2099 and prompts the user to guess the weekday
# It keeps track of the time it takes for each guess and the users score

import random
import time
import datetime
from datetime import datetime
import calendar
import os

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
totaltime = 0
average = 0
play = True

#Game instructions

print("\nWelcome to Hunter's Doomsday Algorithm Checker\n")

print("Doomsday Dates are as follows:\n\t1/3-4\t2/28-29\t  3/14\n\t4/4\t5/9\t  6/6\n\t7/11\t8/8\t  9/5\n\t10/10\t11/7\t  12/12\n")

print('Weekdays can be represented as numbers like so:\n\tSunday = 0\n\tMonday = 1\n\tTuesday = 2\n\tWednesday = 3\n\tThursday = 4\n\tFriday = 5\n\tSaturday = 6\n')

print('Doomsday for 2000 is Tuesday (2) and Doomsday for 1900 is Wednesday (3)\n')

print('Special years:\n\t12 = 1\t24 = 2\t36 = 3\t48 = 4\n\t60 = 5\t72 = 6\t84 = 7\t96 = 8\n')

print("Basic Calculation is: (century + special year + years to guess year + (guess date - closest doomsday date)) % 7 = weekday number\n")

print('Press any key to begin playing:')
input()

# This clears the terminal before playing so the numbers can't be looked at
# It will be different if this is run on Windows but who cares about them?
os.system('clear')

# Gameplay
while play:

    date = random_date('1/1/1900', '12/31/2099', random.random())

    start = time.time()

    print()
    print(date.strftime('%m/%d/%Y'))
    print('\nEnter Weekday:\t (type exit to stop game)')
    weekday_guess = input().capitalize()

    if(weekday_guess.upper() == 'EXIT'):
        play = False
    elif(weekday_guess == calendar.day_name[date.weekday()]):
        print('CORRECT')
        correct += 1
        total += 1
        totaltime += time.time()-start
    else:
        print('INCORRECT - it is a ' + calendar.day_name[date.weekday()])
        total += 1
        totaltime += time.time()-start
    

# Printing out totals and averages
average = correct/total * 100 if total != 0 else 0
print(f'\nScore is: {correct}/{total}')
print(f'\nAverage is: {average:.2f}%')
averagetime = totaltime/total if total != 0 else 0
print(f'\nAverage time is: {averagetime:.2f} seconds')
print()
