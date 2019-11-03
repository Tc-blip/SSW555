'''
US36	List recent deaths	
List all people in a GEDCOM file who died in the last 30 days
TC12    
'''

import datetime as dt


def check__died_in_30(dt_now,dt_death,name):
    if abs((dt_now-dt_death)).days <30:
        print(f"US36 {name} were died in last 30 days, death {abs((dt_now-dt_death)).days} days")
        return f"{name} were died in last 30 days, death {abs((dt_now-dt_death)).days} days"


def list_died_in_30(indi):
    dt_now = dt.datetime.now()
    for i in indi.values():
        if i.Death != 'NA':
            dt_death = dt.datetime.strptime(i.Death, '%d %b %Y') 
            check__died_in_30(dt_now,dt_death,i.Name)

