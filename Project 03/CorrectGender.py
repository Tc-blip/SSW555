'''
Created: 2019-10-18 10:52:44
Author : Jia Wen
Email : jwen6@stevens.edu
Description: US 21: Husband in family should be male and wife in family should be female 
'''

def check_correct_gender(fm,indi):
    for k, v in fm.items():
        if v.Husband_ID != 'NA' and v.Wife_ID != 'NA':
            gender_father = indi[v.Husband_ID].Gender
            gender_mother = indi[v.Wife_ID].Gender
            if correct_gender(gender_father,gender_mother) == 2:
                print(f"Error: In Family " + k + ", Husband has wrong gender!")
            if correct_gender(gender_father,gender_mother) == 3:
                print(f"Error: In Family " + k + ", Wife has wrong gender!")
            if correct_gender(gender_father,gender_mother) == 4:
                print(f"Error: In Family " + k + ", Husband and Wife both have wrong genders!")

            

def correct_gender(gender_father,gender_mother):
    if gender_father == "M" and gender_mother == "F":
        return 1
    if gender_father == "F" and gender_mother == "F":
        return 2
    if gender_father == "M" and gender_mother == "M":
        return 3
    if gender_father == "F" and gender_mother == "M":
        return 4
    