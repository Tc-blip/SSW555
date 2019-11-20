'''
Created: 2019-11-17 10:41:37
Author : Jia Wen
Email : jwen6@stevens.edu
Description: US 20 Aunts and uncles should not marry their nieces or nephews
'''

def check_Aunt_and_Uncles(fm,indi):
    error = set()
    for k, v in fm.items():  
        if v.Husband_ID != "NA":
            husb = indi["".join(v.Husband_ID)]
        if v.Wife_ID != "NA":
            wife = indi["".join(v.Wife_ID)]
        if husb.Child != "None":
            if wife.Child != "None":
                husb_fam = fm[husb.Child]
                wife_fam = fm[wife.Child]
                if husb_fam.Husband_ID != "NA" and husb_fam.Wife_ID != "NA":
                    husb_parents = indi["".join(husb_fam.Husband_ID)], indi["".join(husb_fam.Wife_ID)]
                    for husb_parent in husb_parents:
                        if husb_parent.Child != "None" and "".join(husb_parent.Child) == "".join(wife.Child):
                            print(f"ERROR: US20: In family {k}, Wife {wife.ID} is Husband {husb.ID}'s aunt." )
                            error.add(k)
                if wife_fam.Husband_ID != "NA" and wife_fam.Wife_ID != "NA":
                    wife_parents = indi["".join(wife_fam.Husband_ID)], indi["".join(wife_fam.Wife_ID)]
                    for wife_parent in wife_parents:
                        if wife_parent.Child != "None" and "".join(wife_parent.Child) == "".join(husb.Child):
                            print(f"ERROR: US20: In family {k}, Husband {husb.ID} is Wife {wife.ID}'s uncle.")
                            error.add(k)
    return error

