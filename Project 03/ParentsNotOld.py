"""
SSW555 Sprint 1
Jia Wen
Use Story 12 Parents Not Too Old
"""
from datetime import datetime

def check_parents_not_old(fm,indi):
    for k, v in fm.items():
        if v.Husband_ID != 'NA' and v.Wife_ID != 'NA':
            bd_father = datetime.strptime(indi[v.Husband_ID].Birthday, '%d %b %Y')
            bd_mother = datetime.strptime(indi[v.Wife_ID].Birthday, '%d %b %Y')
            for c in v.Children:
                if indi[c].Birthday != 'NA':
                    bd_child = datetime.strptime(indi[c].Birthday, '%d %b %Y')
                    if parents_not_old(bd_father,bd_mother,bd_child) == 0 :
                        print('ERROR: Individual US12: ' + c + ' is older than his/her father.')
                    if parents_not_old(bd_father,bd_mother,bd_child) == 1:
                        print('ERROR: Individual US12: ' + c + ' is older than his/her mother.')

def parents_not_old(bd_father, bd_mother, bd_child):

        father = datetime.strftime(bd_father, '%d %b %Y')
        mother = datetime.strftime(bd_mother, '%d %b %Y')
        child = datetime.strftime(bd_child, '%d %b %Y')
        diff_father = (abs((bd_father - bd_child).days)) / 365
        diff_mother = (abs((bd_mother - bd_child).days)) / 365
        if diff_father > 80:
            return 0
        elif diff_mother > 60:
            return 1
        else:
            return 2