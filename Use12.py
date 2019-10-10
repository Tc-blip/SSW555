import datetime as dt
from datetime import datetime



def parents_not_old(bd_father,bd_mother, bd_child):

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




def male_last_name(family_last_name,child__last_name):
    if family_last_name == child__last_name:
        return True
    else:
        return False

