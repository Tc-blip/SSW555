from datetime import timedelta
import datetime

'''
KM Sprint 1
US08	Birth after marriage of parents
US09	Birth before death of parents
'''

#US08   Birth after marriage of parents
def birthAfterMarriage(fm, pi):
    for i in fm.values():
        if i.Married != 'NA':
            wedding_date = i.Married
            if i.Divorced != 'NA':
                divorce_date = i.Divorced
            else:
                divorce_date = 'NA'
            for child in i.Children:
                bday = pi[child].BIRT
                if not birthAfterMarriageOfParents(bday, wedding_date, divorce_date):
                    print(f'Error: {pi[child].Name} was born before the parents\'s wedding or more than 9 months after the divorce.')

#US09   Birth before marriage of parents
def birthBeforeDeath(fm, pi):
    for i in fm.values():
        if i.Married != 'NA':
            hus_death = pi[i.Husband_ID].DEAT
            wife_death = pi[i.Wife_ID].DEAT
            for child in i.Children:
                bday = pi[child].BIRT
                if not birthBeforeDeathOfParents(bday, wife_death, hus_death):
                    print(f'Error: {pi[child].Name} was born after the death of the mother or after 9 months after the death of the father')


def birthAfterMarriageOfParents(child_bday, wedding_date, divorce_date):
    child_bday = datetime.datetime.strptime(child_bday, '%d %b %Y')
    wedding_date = datetime.datetime.strptime(wedding_date, '%d %b %Y')
    # Divorce could be empty
    if divorce_date != 'NA':
        # Add 270 days (9 months) to divorce date
        divorce_date = datetime.datetime.strptime(divorce_date, '%d %b %Y') + timedelta(270)
        beforeDivorce = compareDates(child_bday, divorce_date)
    else:
        beforeDivorce = -1

    if compareDates(child_bday, wedding_date) > 0 and beforeDivorce < 0:
        return True
    else:
        return False

def birthBeforeDeathOfParents(child_bday, wife_death, husband_death):
    if child_bday != 'NA':
        child_bday = datetime.datetime.strptime(child_bday, '%d %b %Y')
    else:
        child_bday = 'NA'
    if wife_death != 'NA':
        wife_death = datetime.datetime.strptime(wife_death, '%d %b %Y')
    else:
        wife_death = 'NA'
    # Add 270 days (9 months) to husband's death
    if husband_death != 'NA':
        nineMonthsAfter = datetime.datetime.strptime(husband_death, '%d %b %Y') + timedelta(270)
    else:
        nineMonthsAfter = 'NA'


    if compareDates(child_bday, wife_death) < 0 and compareDates(child_bday, nineMonthsAfter) < 0:
        return True
    else:
        return False

def compareDates(date1, date2):
    '''Takes in 2 dates and compares them. Returns -1 if the first date is earlier, 0 if they're equal, and 1 if the first date is later'''
    if date1== 'NA' and date2 =='NA':
        return 0
    elif date1 =='NA':
        return 1
    elif date2 =='NA':
        return -1
    elif date1 > date2:
        return 1
    elif date1 == date2:
        return 0
    else:
        return -1