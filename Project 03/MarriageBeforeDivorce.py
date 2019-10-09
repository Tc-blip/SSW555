import datetime

def marriage_before_divorce(marriage_date, divorce_date):
    if divorce_date == "NA":
        return True
    else:
        if marriage_date < divorce_date:
            return True
        else:
            return False


