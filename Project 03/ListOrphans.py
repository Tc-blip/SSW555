"""
Chih-Yu Lee
US33
list Orphans
List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file
"""
def listOrphans(fm, indi):
    orphans_list = []
    for individual in indi:
        if indi[individual].Age != 'NA' and int(indi[individual].Age) >= 18:
            continue
        else:
            individual_family_list = indi[individual].Spouse
            if individual_family_list:
                for i in individual_family_list:
                    family = fm[i]
                    parent_dead = check_if_both_parents_died(family,indi)
                if parent_dead == True:
                    orphans_list.append(individual)
    print(f'US33: list Orphans {orphans_list}')
    return orphans_list

def check_if_both_parents_died(family,indi):
    if indi[family.Husband_ID].Alive == 'False' and indi[family.Wife_ID].Alive == 'False':
        return True
    else:
        return False
