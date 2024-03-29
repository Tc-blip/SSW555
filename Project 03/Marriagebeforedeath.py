"""
Chih-Yu Lee
sprint1
Marriage before death:
Marriage should occur before death of either spouse
"""
import datetime as dt

def check_marriage_before_death(fm,pi):
    for family_key in fm: # get family info
        family_ID = fm[family_key]
        husband_ID = family_ID.Husband_ID
        wife_ID = family_ID.Wife_ID
        # check if the ID is 'NA'
        if husband_ID != "NA":
            husband_ID = pi[family_ID.Husband_ID]
        if wife_ID != "NA":
            wife_ID = pi[family_ID.Wife_ID]
        marriage_before_death(family_ID,husband_ID,wife_ID)

def marriage_before_death(family_ID,husband_ID,wife_ID):
    
    marriage_date = family_ID.Married
    if marriage_date == "NA":
        return print(f'ERROR: US05: FAMILY: {family_ID.ID} missing family marriage date!')   

    if husband_ID != "NA":
        husband_death_date = husband_ID.DEAT
    else:
        husband_death_date = "NA"

    if wife_ID != "NA":
        wife_death_date = wife_ID.DEAT
    else:
        wife_death_date = "NA"

    marriage_date = convet_strdate_numdata(marriage_date)
    husband_death_date = convet_strdate_numdata(husband_death_date)
    wife_death_date = convet_strdate_numdata(wife_death_date)
    
    result = check_if_marriage_before_death(marriage_date, husband_death_date, wife_death_date)
    
    if result =='1':
        print(f'ERROR: US05: FAMILY: {family_ID.ID} wife{wife_ID.ID} die before marriage!')
    if result =='2':
        print(f'ERROR: US05: FAMILY: {family_ID.ID} husband{husband_ID.ID} die before marriage!')
    if result =='3':
        print(f'ERROR: US05: FAMILY: {family_ID.ID} both parents die before marriage!')
    
def check_if_marriage_before_death(marriage_date, husband_death_date, wife_death_date):
    # return 1 means wife die before marriage.
    # return 2 means husband die before marriage.
    # return 3 means bot parent die before marriage.
    if marriage_date == "NA":
        return True

    if husband_death_date == "NA" and wife_death_date == "NA":
        return True

    if husband_death_date == "NA" and wife_death_date != "NA":
        if marriage_date < wife_death_date:
            return True
        else:
            return '1'

    if husband_death_date != "NA" and wife_death_date == "NA":
        if marriage_date < husband_death_date:
            return True
        else:
            return '2'

    if husband_death_date != "NA" and wife_death_date != "NA":
        if marriage_date < husband_death_date and marriage_date < wife_death_date:
            return True
        else:
            return '3'
       
    
def convet_strdate_numdata(date):
    if date != "NA":
        date = dt.datetime.strptime(date, '%d %b %Y')
    return date




