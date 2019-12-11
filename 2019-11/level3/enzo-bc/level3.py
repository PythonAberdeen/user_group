import datetime

# define weekdays as dictionary
weekdays = {'Mo': 0, 'Tu': 1, 'We': 2, 'Th': 3, 'Fr': 4, 'Sa': 5, 'Su': 7, 'PH': 8}

# define bank holidays
bank_holidays = ['01/01', '02/01', '10/04', '08/05', '25/05', '03/08', '30/11', '25/12', '26/12']

# define opening hours
opening_hours = 'Mo-Fr 08:00-12:00,13:00-17:30; Sa 08:00-12:00; PH off'

# define date user wants to check
today = datetime.datetime(2019, 1, 1, 13, 31)

""" split opening hours in order to get different periods
    it produces an array with 3 elements 
    [
        'Mo-Fr 08:00-12:00,13:00-17:30',
        'Sa 08:00-12:00',
        'PH off'
    ]
"""
parts = opening_hours.split('; ')

part_arr = []

# try to extract days and times in loop
for item in parts:
    try:
        # extract days and hours
        part = item.split(' ')
        days, hours = part[0], part[1]

        try:
            # try to get days from format Mo-Fr
            day = days.split('-')
            start_day, end_day = weekdays[day[0]], weekdays[day[1]]
        except:
            # if that fails - it is a single day
            start_day, end_day = weekdays[days], weekdays[days]

        try:
            # try to extract morning and afternoon hours
            hour = hours.split(',')
            morning, afternoon = hour[0].split('-'), hour[1].split('-')
            morning_start, morning_end = morning[0], morning[1]
            afternoon_start, afternoon_end = afternoon[0], afternoon[1]
        except:
            # if that fails - it is a single time period
            hour = hours.split('-')
            try:
                # try to get opening and closing hours
                morning_start, morning_end = hour[0], hour[1]
                afternoon_start, afternoon_end = -1, -1
            except:
                # if that fails - it is closed
                morning_start, morning_end = -1, -1
                afternoon_start, afternoon_end = -1, -1

        # add dictionary of tuples to list
        part_arr.append({'days': (start_day, end_day), 'morning': (morning_start, morning_end),
                         'afternoon': (afternoon_start, afternoon_end)})
    except:
        print('Error!')

# set open flag to False - assumption: it is closed as long as it is not explicitly set to open
open = False

# prepare today string to compare with public holidays
today_string = str(today.strftime('%d')) + '/' + str(today.strftime('%m'))

# loop in reversed order through list of previously prepared dictionaries
for time in reversed(part_arr):
    # if today is a bank holiday and there is no morning time it is closed
    if today_string in bank_holidays and time['days'][0] > 7 and time['morning'][0] == -1:
        break
    elif (today.weekday() in range(time['days'][0], time['days'][1] + 1)) or (
            time['days'][0] > 7 and today_string in bank_holidays):
        try:
            # try to split morning time
            morning_start = time['morning'][0].split(':')
            morning_end = time['morning'][1].split(':')

            # and check if user's time includes
            if datetime.time(int(morning_start[0]), int(morning_start[1])) <= today.time() <= datetime.time(
                    int(morning_end[0]), int(morning_end[1])):
                open = True
                break
        except:
            pass

        try:
            # try to split afternoon time
            afternoon_start = time['afternoon'][0].split(':')
            afternoon_end = time['afternoon'][1].split(':')

            # and check if user's time includes
            if datetime.time(int(afternoon_start[0]), int(afternoon_start[1])) <= today.time() <= datetime.time(
                    int(afternoon_end[0]), int(afternoon_end[1])):
                open = True
                break
        except:
            pass

        if time['days'][0] > 7:
            # if user's date is public holiday and do not match then it is closed
            break

print('open') if open else print('closed')
