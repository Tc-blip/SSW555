'''
us37
List recent survivors
List all living spouses and descendants of people in a GEDCOM file who died in the last 30 days
'''

import datetime as dt


def check__died_in_30(dt_now, dt_death, name):
    if abs((dt_now-dt_death)).days < 30:
        return True
    else:
        return False


def list_died_in_30(indi):
    dt_now = dt.datetime.now()
    list_died_person = []

    for i in indi.values():
        if i.Death != 'NA':
            dt_death = dt.datetime.strptime(i.Death, '%d %b %Y')
            if check__died_in_30(dt_now, dt_death, i.Name):
                list_died_person.append(i.ID)
    return list_died_person


def List_recent_survivors(fm, indi):
    list_died_person = list_died_in_30(indi)

    for i in list_died_person:
        list_living_spouses = ""
        list_living_children = []
        if indi[i].Gender == "F":
            for j in indi[i].Spouse:
                if indi[fm[j].Husband_ID].Alive == "True":
                    list_living_spouses = fm[j].Husband_Name

                for k in fm[j].Children:
                    if indi[k].Alive == "True":
                        list_living_children.append(indi[k].Name)

        elif indi[i].Gender == "M":
            for j in indi[i].Spouse:
                if indi[fm[j].Wife_ID].Alive == "True":
                    list_living_spouses = fm[j].Wife_Name

                for k in fm[j].Children:
                    if indi[k].Alive == "True":
                        list_living_children.append(indi[k].Name)

        print(f"ERROR: US37： {indi[i].Name} died in the last 30 days, living spouse {list_living_spouses}, living children {list_living_children}")
        return f"{indi[i].Name} died in the last 30 days, living spouse {list_living_spouses}, living children {list_living_children}"