'''
Created: 2019-10-24 17:56:33
Author : Jia Wen
Email : jwen6@stevens.edu
Description: US 30 List all living married people in a GEDCOM file
'''

def check_list_living_married(fm,indi):
    for k, v in fm.items():
        if list_living_married(v.Married, v.Divorced) is True:
            if indi[v.Husband_ID].Death == "NA" and indi[v.Wife_ID].Death == "NA":
                print(f"US30: In family {k}, {v.Husband_ID} and {v.Wife_ID} are married in {v.Married}")

def list_living_married(a,b):
    if a != 'NA' and b == "NA":
        return True
    else:
        return False
