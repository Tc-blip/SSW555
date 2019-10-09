'''
TC sprint 1
US08	Birth before marriage of parents
US09	Birth before death of parents
'''
import datetime as dt
from dateFunctions import compareDates

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
