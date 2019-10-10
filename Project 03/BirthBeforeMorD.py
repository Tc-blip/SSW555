'''
TC sprint 1
US02	Birth before marriage
US03	Birth before death
'''
import datetime as dt

def compareDates(date1, date2):
    '''Takes in 2 dates and compares them. Returns -1 if the first date is earlier, 0 if they're equal, and 1 if the first date is later'''
    if date1 > date2:
        return 1
    elif date1 == date2:
        return 0
    else:
        return -1

def birth_before_marriage_p(date1,date2):
    dt1 = dt.datetime.strptime(date1, '%d %b %Y')   
    dt2 = dt.datetime.strptime(date2, '%d %b %Y')                                                               
    if compareDates(dt1, dt2) != -1:
        return False
    return True


def birth_before_death_p(date1,date2):
    dt1 = dt.datetime.strptime(date1, '%d %b %Y')   
    dt2 = dt.datetime.strptime(date2, '%d %b %Y')   
    if compareDates(dt1, dt2) != -1:
        return False
    return True
