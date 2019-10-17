'''
US35	List recent births	TC	Coding
List all people in a GEDCOM file who were born in the last 30 days
TC
'''

import datetime as dt

def list_born_in_30(indi):
    dt_now = dt.datetime.now()
    for i in indi.values():
        dt_birth = dt.datetime.strptime(i.Birthday, '%d %b %Y') 
        if (dt_now-dt_birth).days <30:
            print(f"{i.Name} were born in last 30 days, born {(dt_now-dt_birth).days} days ")

