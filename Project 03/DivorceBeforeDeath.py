"""
Author CYL
sprint 2: User story 06
"""
import datetime as dt
def check_divorce_before_death(fm, pi):
    for key in fm:
        family = fm[key]
        family_husban_ID = family.Husband_ID
        family_wife_ID = family.Wife_ID
        family_divorce_date = family.Divorced
        if family_divorce_date == "NA":
            print(f"Family {family.ID} missing devorced date!")
        husban_death_date = get_death_date(pi,family_husban_ID)
        wife_death_date = get_death_date(pi,family_wife_ID)

        check = divorce_before_death(family_divorce_date, husban_death_date, wife_death_date)
        if check == False:
            print()

def divorce_before_death(family_divorce_date, husban_death_date, wife_death_date):
    # return 1 means wife died before marriage!
    # return 2 means husband died before marriage!
    # return 3 means husband and wife both died before marriage! 
    if family_divorce_date == "NA":
        return True

    if husban_death_date == "NA" and wife_death_date == "NA":
        return True

    if husban_death_date == "NA" and wife_death_date != "NA":
        if wife_death_date < family_divorce_date:
            return 1
        else:
            return True

    if husban_death_date != "NA" and wife_death_date == "NA":
        if husban_death_date < family_divorce_date:
            return 2
        else:
            return True
    
    if husban_death_date != "NA" and wife_death_date != "NA":
        if husban_death_date < family_divorce_date and wife_death_date < family_divorce_date:
            return 3
        if husban_death_date < family_divorce_date:
            return 2
        if wife_death_date < family_divorce_date:
            return 1
        else:
            return True
        
def get_death_date(pi,id):
    if id != "NA":
        death_date = pi[id].DEAT
        if death_date != 'NA':
            death_date = dt.datetime.strptime(death_date, '%d %b %Y')
    else:
        death_date = "NA"
    return death_date

