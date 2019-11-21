'''
Created: 2019-11-17 13:30:32
Author : Jia Wen
Email : jwen6@stevens.edu
Description: US26 Corresponding EntriesAll 
            family roles (spouse, child) specified in an individual record should 
            have corresponding entries in the corresponding family records. Likewise, 
            all individual roles (spouse, child) specified in family records should 
            have corresponding entries in the corresponding  individual's records.  
            I.e. the information in the individual and family records should be consistent.
'''

def check_Corresponding_Entries(fm,indi):
    result = set()
    for k,v in indi.items():
        if v.Child is "None" and v.Spouse == []:
            print(f"ERROR: US26: Individual {k} doesn't have any corresponding records in any family.")
            result.add(k)
        if v.Spouse != []:
            for i in v.Spouse:
                fam = fm[i]
            if fam.Husband_ID != k and fam.Wife_ID != k:
                print(f"ERROR: US26: In family {fam.ID} , individual {k} does not have corresponding record as spouse.")
                result.add(k)
        if v.Child != "None":
            fam = fm[v.Child]
            if k not in fam.Children:
                print(f"ERROR: US26: In family {fam.ID} , individual {k} does not have corresponding record as child.")
                result.add(k)
    return result

           