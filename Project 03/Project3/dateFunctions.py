import datetime as dt

def compareDates(date1, date2):
    '''Takes in 2 dates and compares them. Returns -1 if the first date is earlier, 0 if they're equal, and 1 if the first date is later'''
    if date1 > date2:
        return 1
    elif date1 == date2:
        return 0
    else:
        return -1

def dateBeforeCurrentDate(date1):
    if compareDates(date1, dt.datetime.now()) != -1:
        return False
    return True

def differenceBetweenDates(date1, date2):
    '''Takes in 2 dates and returns date1-date2 in years'''
    delta = date2-date1
    delta = delta.total_seconds()
    years = (((delta/3600)/24)/365)
    return years

def lessThan150YearsOld(date1):
    if differenceBetweenDates(date1, dt.datetime.now()) < 150:
        return True
    else:
        return False
