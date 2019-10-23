import datetime as dt
from datetime import timedelta

from dateFunctions import compareDates

# US28

def getAge(child):
    return child.Age

def listSiblings(children):
    ''' List siblings by decreasing age, i.e, oldest siblings first '''
    if len(children) == 0:
        return []
    child_list = children
    child_list.sort(reverse=True, key=getAge)
    return child_list

#US13

def check_siblingSpacing(fm, pi):
    for family in fm.values():
        if len(family.Children) == 0:
            return
        else:
            new_child_list = []
            for childID in family.Children:
                new_child_list.append(pi[childID])
            if not siblingSpacing(new_child_list):
                print(f'Error: Children should not be born more than 2 days or less than 8 months apart')

def siblingSpacing(children):
    ''' Birthdays should be more than 8 months apart or less than 2 days apart '''
    sibling_list = listSiblings(children)
    i = 1
    for child1 in sibling_list:
        child1_bday = dt.datetime.strptime(child1.Birthday, '%d %b %Y')
        for child2 in sibling_list[i:]:
            eightMonthsBefore = dt.datetime.strptime(child2.Birthday, '%d %b %Y') - timedelta(240) # 240 = 8 months * 30 days
            twoDaysBefore = dt.datetime.strptime(child2.Birthday, '%d %b %Y') - timedelta(2)
            #Children can't be born more than 2 days or less than 8 months apart
            if compareDates(child1_bday, eightMonthsBefore) > 0 or compareDates(child1_bday, twoDaysBefore) > 0:
                return False
        i += 1
    return True