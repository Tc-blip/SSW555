"""
Liam King

"""

from dateFunctions import compareDates
import datetime as dt

def noBigamy(fm):
    """Returns true if bigamy has not occurred, false if it has"""
    bigamy = 0
    for key in fm:
        family = fm[key]
        husband_id = family.Husband_ID
        wife_id = family.Wife_ID
        for key2 in fm:
            if key2 != key:
                family2 = fm[key2]
                husband_id2 = family2.Husband_ID
                wife_id2 = family2.Wife_ID
                if husband_id == husband_id2:
                    if family.Divorced != "NA":
                        div_date = dt.datetime.strptime(family.Divorced, '%d %b %Y')
                        mar_date = dt.datetime.strptime(family2.Married, '%d %b %Y')
                        if compareDates(div_date, mar_date) != -1:
                            print("ERROR: US11: " + fm[key].Husband_Name + " " + husband_id + " in family " + fm[key].ID + " married again before getting a divorce.")
                            bigamy += 1
                    if family2.Divorced != "NA":
                        div_date = dt.datetime.strptime(family2.Divorced, '%d %b %Y')
                        mar_date = dt.datetime.strptime(family.Married, '%d %b %Y')
                        if compareDates(div_date, mar_date) != -1:
                            print("ERROR: US11: " + fm[key2].Husband_Name + " " + husband_id2 + " in family " + fm[key2].ID + " married again before getting a divorce.")
                            bigamy += 1
                if wife_id == wife_id2:
                    if family.Divorced != "NA":
                        div_date = dt.datetime.strptime(family.Divorced, '%d %b %Y')
                        mar_date = dt.datetime.strptime(family2.Married, '%d %b %Y')
                        if compareDates(div_date, mar_date) != -1:
                            print("ERROR: US11: " + fm[key].Wife_Name + " " + wife_id + " in family " + fm[key].ID + " married again before getting a divorce.")
                            bigamy += 1
                    if family2.Divorced != "NA":
                        div_date = dt.datetime.strptime(family2.Divorced, '%d %b %Y')
                        mar_date = dt.datetime.strptime(family.Married, '%d %b %Y')
                        if compareDates(div_date, mar_date) != -1:
                            print("ERROR: US11: " + fm[key].Wife_Name + " " + wife_id2 + " in family " + fm[key2].ID + " married again before getting a divorce.")
                            bigamy += 1
    return bigamy == 0

def marriageAfter14(fm, pi):
    """Returns true if all spouses got married after 14, false if not"""
    notOkay = 0
    for key in fm:
        family = fm[key]
        if(family.Married != "NA"):
            marriage_date = dt.datetime.strptime(family.Married, '%d %b %Y')
            husband_id = family.Husband_ID
            husband_birthday_plus_14 = dt.datetime.strptime(pi[husband_id].BIRT, '%d %b %Y') + dt.timedelta(days=5110)
            wife_id = family.Wife_ID
            wife_birthday_plus_14 = dt.datetime.strptime(pi[wife_id].BIRT, '%d %b %Y') + dt.timedelta(days=5110)
            if compareDates(husband_birthday_plus_14, marriage_date) != -1:
                print("ERROR: US10: Marriage date of " + family.Husband_Name + " " + "(" + husband_id + ") is before " + family.Husband_Name + " reaches 14 years of age.")
                notOkay += 1
            if compareDates(wife_birthday_plus_14, marriage_date) != -1:
                print("ERROR: US10: Marriage date of " + family.Wife_Name + " " + "(" + wife_id + ") is before " + family.Wife_Name + " reaches 14 years of age.")
                notOkay += 1
    return notOkay == 0



