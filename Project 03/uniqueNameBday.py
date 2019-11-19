# US23
# No more than one individual with the same name and birth date should appear in a GEDCOM file
import collections

def check_uniqueNameBday(pi):
    nameBdayList = []
    for key in pi:
        person = pi[key]
        nameBday = person.NAME + person.BIRT
        nameBdayList.append(nameBday)
    uniqueNameBday(nameBdayList)

def uniqueNameBday(bdayList):
    dup_nameBday = [item for item, count in collections.Counter(bdayList).items() if count > 1]
    for id in dup_nameBday:
        print(f"US23 ERROR: Duplicate name and birthday pair found: {dup_nameBday}!")
