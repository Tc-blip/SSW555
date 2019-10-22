"""
SSW555 Sprint 1
Jia Wen
Use Story 16 Male Last NAme
"""

def check_male_last_name(fm,indi):
    for k, v in fm.items():
        family_last_name = indi[v.Husband_ID].Name.split('/')[1]
        for i in v.Children:
            if indi[i].Gender == 'M':
                child_last_name = indi[i].Name.split('/')[1]
                if male_last_name(family_last_name,child_last_name) is False:
                    print('ERROR: INDIVIDUAL US16' + indi[i].ID + ': has last name ' + child_last_name +
                      ' which is different from the family last name: ' + family_last_name)


def male_last_name(family_last_name,child__last_name):
    if family_last_name == child__last_name:
        return True
    else:
        return False
