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
                    if father_not_old(bd_father,bd_child) is True:
                        print(f"ERROR: US12: In family {k}，Husband {v.Husband_ID} is more than 80 years old than his child {indi[c].ID}.")
                    if mother_not_old(bd_mother,bd_child) is True:
                        print(f"ERROR: US12: In family {k}, Wife {v.Wife_ID} is more than 60 years old than her child {indi[c].ID}.")

def father_not_old(bd_father, bd_child):

    diff_father = (abs((bd_father - bd_child).days)) / 365
    if diff_father > 80:
        return True
    else:
        return False

def mother_not_old(bd_mother,bd_child):

    diff_mother = (abs((bd_mother - bd_child).days)) / 365
    if diff_mother > 60:
        return True
    else:
        return False
