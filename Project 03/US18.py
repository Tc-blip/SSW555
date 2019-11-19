'''
US18
Liam King
Returns IDs of married siblings
'''

def noSiblingMarriage(fam):
    marriedSiblings = []
    for key in fam:
        family = fam[key]
        husbandID = family.Husband_ID
        husbandName = family.Husband_Name
        wifeID = family.Wife_ID
        wifeName = family.Wife_Name
        for siblingCheckKey in fam:
            if husbandID in fam[siblingCheckKey].Children and wifeID in fam[siblingCheckKey].Children:
                print("ERROR: US18: " + husbandName + " (" + husbandID + ") and " + wifeName + " (" + wifeID + ") are siblings and are married.")
                marriedSiblings.append(husbandID)
                marriedSiblings.append(wifeID)
    return marriedSiblings