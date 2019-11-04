"""
Chih-Yu Lee
sprint 3
List upcoming birthdays:
List all living people in a GEDCOM file whose birthdays occur in the next 30 days
"""
import datetime as dt

def ListUpcomingBirthdays(pi):
    upcomingBdaylist = []
    dt_now = dt.datetime.now()
    for i in pi:
        if pi[i].DEAT == 'NA':
            people_bithday = pi[i].BIRT
            people_bithday = dt.datetime.strptime(people_bithday,"%d %b %Y")
            pb = convert_to_same_year(people_bithday)
            days = (pb - dt_now).days
            if days <= 30 and days >0:
                upcomingBdaylist.append(pi[i].ID)
    print(f"All living people whose birthdays occur in the next 30 days {upcomingBdaylist}")
    return upcomingBdaylist
    

def convert_to_same_year(md):
    dt_now = dt.datetime.now()
    if md.year != dt_now.year and md.year < dt_now.year:
        year_delta = (dt_now.year - md.year)
        md = md.replace(year = (md.year + year_delta))
    return md
