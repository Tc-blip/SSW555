"""
List all living couples in a GEDCOM file whose marriage anniversaries occur in the next 30 days
"""
import datetime as dt

def ListUpcomingAnniversaries(fm, indi):
    upcomingAdaylist = []
    for key in fm:
        family = fm[key]
        fm_marriage_date = family.Married

        if check_if_living_couple(family, indi) == False:
            continue
        if fm_marriage_date == "NA":
            continue
        A_day = dt.datetime.strptime(fm_marriage_date,"%d %b %Y")
        A_day = convert_to_same_year(A_day)

        if check_if_occur_in_30_days(A_day) == True:
            upcomingAdaylist.append(key)
    print(f"All living couples whose marriage anniversaries occur in the next 30 days {upcomingAdaylist}")
    return upcomingAdaylist

def check_if_living_couple(family,indi):
    wifeID = family.Wife_ID
    husbandID = family.Husband_ID
    if wifeID == "NA" or husbandID == "NA":
        print(f"Famile {family.ID} missing wife ID")
        return False

    w_alive = indi[wifeID].Alive
    h_alive = indi[husbandID].Alive
    if w_alive != "True" or h_alive != "True":
        return False
    return True

def check_if_occur_in_30_days(marriage_date):
    dt_now = dt.datetime.now()
    delt_day = (marriage_date - dt_now).days
    if delt_day <= 30 and delt_day > 0:
        return True
    else:
        return False

def convert_to_same_year(md):
    dt_now = dt.datetime.now()
    year = (dt_now - md).days
    year = int(year/365)
    if md.month >dt_now.month:
        year += 1
    md = md.replace(year = md.year + year)
    return md