from dateFunctions import differenceBetweenDates, compareDates
import datetime as dt

def listLargeAgeDifferences(fam, indi):
    largeAgeDiffCouples = []
    for key in fam:
        family = fam[key]
        if family.Married != "NA":
            marriage_date = dt.datetime.strptime(family.Married, '%d %b %Y')
            wife = indi[family.Wife_ID]
            husband = indi[family.Husband_ID]
            wife_birthday = dt.datetime.strptime(wife.Birthday, '%d %b %Y')
            husband_birthday = dt.datetime.strptime(husband.Birthday, '%d %b %Y')

            wife_age_at_wedding = differenceBetweenDates(wife_birthday, marriage_date)
            husband_age_at_wedding = differenceBetweenDates(husband_birthday, marriage_date)

            if compareDates(wife_birthday, husband_birthday) == -1:
                #wife is older
                if wife_age_at_wedding >= husband_age_at_wedding*2:
                    print("US34: Individuals " + husband.ID + " and " + wife.ID + " were married when individual " + wife.ID + " was at least twice as old as individual " + husband.ID)
                    largeAgeDiffCouples.append([husband.ID, wife.ID])

            elif compareDates(wife_birthday, husband_birthday) == 1:
                #husband is older
                if husband_age_at_wedding >= wife_age_at_wedding*2:
                    print("US34: Individuals " + husband.ID + " and " + wife.ID + " were married when individual " + husband.ID + " was at least twice as old as individual " + wife.ID)
                    largeAgeDiffCouples.append([husband.ID, wife.ID])
    return largeAgeDiffCouples

