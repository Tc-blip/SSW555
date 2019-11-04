'''
US24
Unique families by spouses
No more than one family with the same spouses by name and the same marriage date should appear in a GEDCOM file
'''



def check_unique_fm_by_spouses(fm):
    family_list = []
    for i in fm.values():
        if (i.Married,i.Husband_Name,i.Wife_Name) not in family_list:
            family_list.append((i.Married, i.Husband_Name, i.Wife_Name))
        else:
            print(f"US24 Error, same has already in GEDCOM {(i.Married,i.Husband_Name,i.Wife_Name)}")
            return f"Error, same has already in GEDCOM {(i.Married,i.Husband_Name,i.Wife_Name)}"