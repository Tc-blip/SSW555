"""
Chih-Yu Lee
US33
list Orphans
List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file
"""
def listOrphans(fm, indi):
    orphans_list = []
    for individual in indi:
        if int(indi[individual].Age) >= 18:
            continue
        else:
            print(individual)
    return orphans_list

def check_if_both_parents_dead(fm,familyID):
    

    return True


def check_if_child_under_18():

    return True