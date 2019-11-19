'''
US19
Liam King
Returns true if there are no occurrences of first cousins being married, false if such occurrences exist
'''

def noCousinMarriage(fam):
    noBadMarriages = True
    for key in fam:
        family = fam[key]
        husbandID = family.Husband_ID
        husbandName = family.Husband_Name
        wifeID = family.Wife_ID
        wifeName = family.Wife_Name
        husbandFirstCousins = findFirstCousins(husbandID, fam)
        if not husbandFirstCousins == -1 and not husbandFirstCousins == None:
            for item in husbandFirstCousins:
                if not item == -1:
                    if wifeID in item:
                        print("ERROR: US19: " + husbandName + " (" + husbandID + ") and " + wifeName + " (" + wifeID + ") are first cousins and are married.")
                        noBadMarriages = False
        wifeFirstCousins = findFirstCousins(wifeID, fam)
        if not wifeFirstCousins == -1 and not wifeFirstCousins == None:
            for item in wifeFirstCousins:
                if not item == -1:
                    if husbandID in item:
                        print("ERROR: US19: " + husbandName + " (" + husbandID + ") and " + wifeName + " (" + wifeID + ") are first cousins and are married.")
                        noBadMarriages = False
    return noBadMarriages


def findFirstCousins(id, fam):
    '''Takes in an id and finds that person's first cousins if they exist, -1 otherwise'''
    firstCousins = []
    for key in fam:
        family = fam[key]
        if id in family.Children:
            fatherID = family.Husband_ID
            motherID = family.Wife_ID
            fatherSiblings = findSiblings(fatherID, fam)
            if not fatherSiblings == -1 and not fatherSiblings == None:
                for item in fatherSiblings:
                    firstCousins.append(findChildren(item, fam))
            motherSiblings = findSiblings(motherID, fam)
            if not motherSiblings == -1 and not motherSiblings == None:
                for item in motherSiblings:
                    firstCousins.append(findChildren(item, fam))
            return firstCousins
    return -1

def findSiblings(id, fam):
    '''Takes in an id and finds that person's siblings if they exist, -1 otherwise'''
    for key in fam:
        family = fam[key]
        if id in family.Children:
            siblings = family.Children
            return siblings
    return -1

def findChildren(id, fam):
    '''Takes in an id and finds that person's children if they exist, -1 otherwise'''
    for key in fam:
        family = fam[key]
        if family.Husband_ID == id or family.Wife_ID == id:
            return family.Children
    return -1