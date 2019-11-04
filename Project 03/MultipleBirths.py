"""
Autor: CHIH-YU LEE
User story 13
No more than five siblings should be born at the same time
"""
import datetime

def multiple_birth(fm,pi):
    for key in fm:
        family = fm[key]
        children = family.Children
        child_birth_dict = check_children_birthday(children,pi)
        check = check_if_more_than_5_children(child_birth_dict)
        if check == False:
            print(f'Family {family.ID} has more than five siblings born at the same time!')

def check_children_birthday(children,pi):
    child_birth_dict = {}
    for child in children:
        child_birthday = pi[child].BIRT
        if child_birthday not in child_birth_dict:
            child_birth_dict[child_birthday] = 1
        else:
            child_birth_dict[child_birthday] += 1
    return child_birth_dict

def check_if_more_than_5_children(child_birth_dict):
    if child_birth_dict:
        for bithday_children_num in child_birth_dict.values():
            if not bithday_children_num <= 5:
                return False
            else:
                return True
    else:
        return True
    
    

        
