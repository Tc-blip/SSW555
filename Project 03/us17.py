'''
US17
No marriages to descendants	
Parents should not marry any of their descendants
'''

def NoMarrDesc(fm,indi):
    for i in fm.values():
        if i.Husband_ID != "NA" and i.Wife_ID != "NA":
            if indi[i.Husband_ID].Child != "None":
                for j in i.Children:
                    if i.Wife_ID == j:
                        print(f"Error US17: in {i.ID} Parents should not marry any of their descendants")
        
            if indi[i.Wife_ID].Child != "None":    
                for j in i.Children:
                    if i.Husband_ID == j:
                        print(f"Error US17: in {i.ID} Parents should not marry any of their descendants")