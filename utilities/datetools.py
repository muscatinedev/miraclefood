import calendar
from django.shortcuts import render
from datetime import datetime, timedelta, date

today = date.today()


def startThisWeek():
    return date.today() - timedelta(days=today.weekday())
def endThisWeek():
    return date.today() - timedelta(days=today.weekday()+6)




def endPrevWeek():
    return date.today() - timedelta(days=today.weekday()+1)

def startPrevWeek():
    lastday=date.today() - timedelta(days=today.weekday()+1)
    return lastday - timedelta(days=lastday.weekday())


def startThisMonth():
    input_dt = datetime.today().date()
    print('Input date:', input_dt)

    # get the actual day number
    day_num = input_dt.strftime("%d")

    # subtract those number of days from input date
    # using the timedelta
    res = date.today() - timedelta(days=int(input_dt.strftime("%d")) - 1)
    return res

def endThisMonth():
    last_day = date.today().replace(day=calendar.monthrange(date.today().year, date.today().month)[1])
    return last_day




def startPrevMonth():
    # first replace day number with 1
    dt = date.today().replace(day=1)

    # subtract 1 day from input datetime
    # go back to previous month i.e. last date of previous month
    dt = dt - timedelta(days=1)

    # replace day number with 1
    res = dt.replace(day=1)

    return res


def lastPrevMonth():
    # first replace day number with 1
    dt = date.today().replace(day=1)

    # subtract 1 day from input datetime
    # go back to previous month i.e. last date of previous month
    res = dt - timedelta(days=1)

    return res

def firstdayYear():



    starting_day_of_current_year = datetime.now().date().replace(month=1, day=1)
    ending_day_of_current_year = datetime.now().date().replace(month=12, day=31)

    return starting_day_of_current_year



