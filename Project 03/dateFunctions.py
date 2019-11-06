import datetime as dt

def compareDates(date1, date2):
    '''Takes in 2 dates and compares them. Returns -1 if the first date is earlier, 0 if they're equal, and 1 if the first date is later'''
    if date1 > date2:
        return 1
    elif date1 == date2:
        return 0
    else:
        return -1

def dateBeforeCurrentDate(fm, indi):
    """Returns true if there is an invalid date, false if not"""
    rightNow = dt.datetime.now()
    invalidDate = 0
    for key in fm:
        family = fm[key]
        if family.Married != "NA":
            marriage_date = dt.datetime.strptime(family.Married, '%d %b %Y')
            if compareDates(marriage_date, rightNow) != -1:
                print("ERROR: US01: Marriage date of family " + family.ID + " is not before the current date.")
                invalidDate += 1
        if family.Divorced != "NA":
            divorce_date = dt.datetime.strptime(family.Divorced, '%d %b %Y')
            if compareDates(divorce_date, rightNow) != -1:
                print("ERROR: US01: Divorce date of family " + family.ID + " is not before the current date.")
                invalidDate += 1

    for key in indi:
        individual = indi[key]
        birth_date = dt.datetime.strptime(individual.Birthday, '%d %b %Y')
        if compareDates(birth_date, rightNow) != -1:
            print("ERROR: US01: Birth date of  " + individual.Name + " " + "(" + individual.ID + ") is not before the current date.")
            invalidDate += 1
        if individual.Death != "NA":
            death_date = dt.datetime.strptime(individual.Death, '%d %b %Y')
            if compareDates(death_date, rightNow) != -1:
                print("ERROR: US01: Death date of  " + individual.Name + " " + "(" + individual.ID + ") is not before the current date.")
                invalidDate += 1

    return invalidDate != 0

def differenceBetweenDates(date1, date2):
    '''Takes in 2 dates and returns date1-date2 in years'''
    delta = date2-date1
    delta = delta.total_seconds()
    years = (((delta/3600)/24)/365)
    return years

def lessThan150YearsOld(indi):
    """Returns true if all relevant dates are good, false if not"""
    allDatesGood = 0
    rightNow = dt.datetime.now()
    for key in indi:
        individual = indi[key]
        birth_date = dt.datetime.strptime(individual.Birthday, '%d %b %Y')
        if differenceBetweenDates(rightNow, birth_date) > 150:
            if individual.Death != "NA":
                death_date = dt.datetime.strptime(individual.Death, '%d %b %Y')
                if differenceBetweenDates(death_date, birth_date) >= 150:
                    print("ERROR: US07: Death date of  " + individual.Name + " " + "(" + individual.ID + ") is at least 150 years after birth.")
                    allDatesGood += 1
            else:
                if differenceBetweenDates(rightNow, birth_date) >= 150:
                    print("ERROR: US07: Birth date of  " + individual.Name + " " + "(" + individual.ID + ") is at least 150 years ago and " + individual.Name + " is still alive.")
                    allDatesGood += 1
    return allDatesGood == 0