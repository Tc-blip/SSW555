'''
US08	Birth before marriage of parents
US09	Birth before death of parents
'''

import datetime as dt
from dateFunctions import compareDates

def birth_before_marriage_p(date1,date2):
    if compareDates(date1, date2) != -1:
        return False
    return True


def birth_before_death_p(date1,date2):
    if compareDates(date1, date2) != -1:
        return False
    return True
