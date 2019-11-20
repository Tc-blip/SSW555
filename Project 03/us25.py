"""
Unique first names in families
No more than one child with the same name and birth date should appear in a family
"""


def check_unique_first_name_fm(fm,indi):
    child_list = []
    for i in fm.values():
        for j in i.Children:
            if (j,indi[j].Birthday) not in child_list:
                child_list.append((j,indi[j].Birthday))
            else:
                print(f"ERROR: US25: child with the same name and birth date should appear in a family {i.ID}, child id is {j}")
        
