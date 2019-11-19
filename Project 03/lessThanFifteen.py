# US15
# There should be fewer than 15 siblings in a family

def check_lessThanFifteen(familyList):
    for key in familyList:
        family = familyList[key]
        if not lessThanFifteen(family.Children):
            print("US15 Error: There should be fewer than 15 siblings in a family")

def lessThanFifteen(children):
    if len(children) > 15:
        return False
    else:
        return True