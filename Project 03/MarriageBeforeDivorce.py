import datetime as dt

def check_marriage_before_divorce(fm):
    for family_key in fm: # get family info
        marriage_date = fm[family_key].Married
        divorced_date = fm[family_key].Divorced 

        # convet datatime to number form
        if marriage_date != 'NA': 
            marriage_date = dt.datetime.strptime(marriage_date, '%d %b %Y')
        if divorced_date != 'NA':
            divorced_date = dt.datetime.strptime(divorced_date, '%d %b %Y')

        #check if marriage_before_divorce
        if marriage_before_divorce(marriage_date, divorced_date) == False:
            print(f'errors! family {family_key} marriage after divorce!' )

def marriage_before_divorce(marriage_date, divorce_date):
    if divorce_date == "NA":
        return True
    else:
        if marriage_date < divorce_date:
            return True
        else:
            return False


