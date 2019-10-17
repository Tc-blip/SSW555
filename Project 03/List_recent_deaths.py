'''
US36	List recent deaths	
List all people in a GEDCOM file who died in the last 30 days
TC12    
'''

import datetime as dt


def list_died_in_30(indi):
    dt_now = dt.datetime.now()
    for i in indi.values():
        if i.Death != 'NA':
            dt_death = dt.datetime.strptime(i.Death, '%d %b %Y') 
            if (dt_now-dt_death).days <30:
                print(f"{i.Name} were died in last 30 days, born {(dt_now-dt_death).days} days ")


