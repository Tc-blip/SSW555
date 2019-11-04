'''
US35	List recent births	TC	Coding
List all people in a GEDCOM file who were born in the last 30 days
TC
'''

import datetime as dt


def check__born_in_30(dt_now,dt_birth,name):
    if abs((dt_now-dt_birth)).days <30:
        print(f"US 35 {name} were born in last 30 days, born {abs((dt_now-dt_birth)).days} days")
        return f"{name} were born in last 30 days, born {abs((dt_now-dt_birth)).days} days"

def list_born_in_30(indi):
    dt_now = dt.datetime.now()
    for i in indi.values():
        dt_birth = dt.datetime.strptime(i.Birthday, '%d %b %Y') 
        check__born_in_30(dt_now,dt_birth,i.Name)

