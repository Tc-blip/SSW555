'''
TC sprint 1
US08	Birth before marriage of parents
US09	Birth before death of parents
'''
import datetime as dt


def compareDates(date1, date2):
    '''Takes in 2 dates and compares them. Returns -1 if the first date is earlier, 0 if they're equal, and 1 if the first date is later'''
    if date1 > date2:
        return 1
    elif date1 == date2:
        return 0
    else:
        return -1


#US08	Birth before marriage of parents
def check_Birth_before_marr(fm,pi):
    for i in fm.values():
        # check hus birthday before marr
        hus_birthday = pi[i.Husband_ID].BIRT
        if i.Married != 'NA':
            if not birth_before_marriage_p(hus_birthday,i.Married):
                print(f'Error {i.Husband_Name} birthday_before_marr birthday{hus_birthday}  married{i.Married}')
        
        #check wife birthday before marr
        if i.Wife_ID != 'NA':
            wife_birthday = pi[i.Wife_ID].BIRT
            if not birth_before_marriage_p(wife_birthday,i.Married):
                print(f'Error {i.Wife_Name} birthday_before_marr birthday {wife_birthday}  married {i.Married}')
      

def birth_before_marriage_p(date1,date2):
    dt1 = dt.datetime.strptime(date1, '%d %b %Y')   
    dt2 = dt.datetime.strptime(date2, '%d %b %Y')                                                               
    if compareDates(dt1, dt2) != -1:
        return False
    return True


#US09	Birth before death of parents
def check_Birth_before_death(indi):
    for i in indi.values():
        if i.Death != 'NA':
            if not birth_before_death_p(i.Birthday,i.Death):
                print(f'Error {i.Name} birthday_before_marr birthday {i.Birthday}  Death {i.Death}')


def birth_before_death_p(date1,date2):
    dt1 = dt.datetime.strptime(date1, '%d %b %Y')   
    dt2 = dt.datetime.strptime(date2, '%d %b %Y')   
    if compareDates(dt1, dt2) != -1:
        return False
    return True
