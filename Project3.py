import unittest

from prettytable import PrettyTable
import datetime as dt
from datetime import datetime
from dateFunctions import compareDates, dateBeforeCurrentDate, differenceBetweenDates, lessThan150YearsOld
import unittest

class Person_info:
    __slots__ = ["ID",'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS']

    def __init__(self,id):
        self.ID = id
        self.NAME = ""
        self.SEX = ""
        self.BIRT = ""
        self.DEAT = "NA"
        self.FAMC = ""
        self.FAMS = ""

    def add_name(self,name):
        self.NAME = name

    def add_sex(self,sex):
        self.SEX= sex

    def add_birth(self,birth):
        self.BIRT = birth

    def add_deat(self, deat):
        self.DEAT = deat

    def add_famc(self,famc):
        self.FAMC = famc

    def add_fams(self,fams):
        self.FAMS = fams


class Individuals:
    __slots__ = ["ID","Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    def __init__(self,id):
        self.ID = id
        self.Name = ""
        self.Gender = ""
        self.Birthday = ""
        self.Age = ""
        self.Alive = "True"
        self.Death = "NA"
        self.Child = "None"
        self.Spouse = []

    def add_name(self,id):
        self.Name = pi[id].NAME

    def add_gender(self,id):
        self.Gender = pi[id].SEX

    def add_birth(self,id):
        self.Birthday = pi[id].BIRT

    def add_age(self):
        dt1 = dt.datetime.strptime(self.Birthday, '%d %b %Y')
        if not dateBeforeCurrentDate(dt1):
            print(self.Name + "'s birthday is not before the current date.")
        else:
            if not lessThan150YearsOld(dt1):
                print(self.Name + " is older than 150 years old.")
        if self.Alive == "False":
            dt2 = dt.datetime.strptime(self.Death, '%d %b %Y')
            if not dateBeforeCurrentDate(dt2):
                print(self.Name + "'s death is not before the current date.")
            else:
                if differenceBetweenDates(dt2, dt1) > 150:
                    print(self.Name + " lived to be longer than 150 years old.")
        else:
            dt2 = dt.datetime.now()
        self.Age = ((dt2 - dt1).days) // 365

    def add_alive(self):
        if self.Death == "NA":
            self.Alive = "True"
        else:
            self.Alive = "False"

    def add_deat(self,id):
        self.Death = pi[id].DEAT

    def add_chil(self,id):
        for i in fm.values():
            if id in i.Children:
                self.Child = i.ID

    def add_spouse(self,id):
        for i in fm.values():
            if id == i.Husband_ID or id == i.Wife_ID:
                self.Spouse.append(i.ID)

    def pt(self):
        yield self.ID, self.Name, self.Gender, self.Birthday, self.Age, self.Alive, self.Death, self.Child, self.Spouse


class Families:
    __slots__ = ["ID", "Married", "Divorced", "Husband_ID", "Husband_Name", "Wife_ID",
                 "Wife_Name", "Children"]
    def __init__(self,id):
        self.ID = id
        self.Married = "NA"
        self.Divorced = "NA"
        self.Husband_ID = "NA"
        self.Husband_Name = "NA"
        self.Wife_ID = "NA"
        self.Wife_Name = "NA"
        self.Children = []

    def add_marr(self,marr):
        self.Married = marr
        dt1 = dt.datetime.strptime(self.Married, '%d %b %Y')
        if not dateBeforeCurrentDate(dt1):
            print(self.ID + "'s marriage is not before the current date.")
    def add_husb(self,husb):
        self.Husband_ID = husb
    def add_husb_name(self,id):
        self.Husband_Name = pi[id].NAME
    def add_wife(self,wife):
        self.Wife_ID = wife
    def add_wife_name(self,id):
        self.Wife_Name = pi[id].NAME
    def add_chil(self,chil):
        self.Children.append(chil)
    def add_div(self,div):
        self.Divorced = div
        dt1 = dt.datetime.strptime(self.Divorced, '%d %b %Y')
        if not dateBeforeCurrentDate(dt1):
            print(self.ID + "'s divorce is not before the current date.")

    def pt(self):
        yield self.ID, self.Married,self.Divorced,self.Husband_ID, self.Husband_Name, self.Wife_ID, self.Wife_Name, self.Children

def file_reader(path):
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(f"Can't open {path}")
    else:
        with fp:
            for line in fp:
                line = line.rstrip('\n')
                yield line


pi = {}
indi = {}
fm = {}

def read_person(path):
    fp = file_reader(path)

    for i in fp:
        new_i = i.split()
        if new_i[0] == "0":
            if "INDI" in new_i:
                pi[new_i[1]] = Person_info(new_i[1])
                id = new_i[1]
            if "FAM" in new_i:
                fm[new_i[1]] = Families(new_i[1])
                id = new_i[1]
        else:
            if new_i[1] == "NAME":
                pi[id].add_name(" ".join(new_i[2:]))
            elif new_i[1] == "SEX":
                pi[id].add_sex(new_i[2])
            elif new_i[1] == "BIRT":
                new_i = new_i = next(fp).split()
                pi[id].add_birth(" ".join(new_i[2:]))
            elif new_i[1] == "DEAT":
                new_i = new_i = next(fp).split()
                pi[id].add_deat(" ".join(new_i[2:]))
            elif new_i[1] == "FAMC":
                pi[id].add_famc(new_i[2])
            elif new_i[1] == "FAMS":
                pi[id].add_famc(new_i[2])
            elif new_i[1] == "MARR":
                new_i = new_i = next(fp).split()
                fm[id].add_marr(" ".join(new_i[2:]))
            elif new_i[1] == "HUSB":
                fm[id].add_husb(new_i[2])
            elif new_i[1] == "WIFE":
                fm[id].add_wife(new_i[2])
            elif new_i[1] == "CHIL":
                fm[id].add_chil(new_i[2])
            elif new_i[1] == "DIV":
                new_i = new_i = next(fp).split()
                fm[id].add_div(" ".join(new_i[2:]))

def add_infor():
    for i in fm.values():
        if i.Wife_ID != "NA":
            i.add_wife_name(i.Wife_ID)
        if i.Husband_ID != "NA":
            i.add_husb_name(i.Husband_ID)

    for key,value in pi.items():
        indi[key] = Individuals(key)
        indi[key].add_name(key)
        indi[key].add_gender(key)
        indi[key].add_birth(key)
        indi[key].add_deat(key)
        indi[key].add_chil(key)
        indi[key].add_spouse(key)
        indi[key].add_alive()
        indi[key].add_age()

def pt_fm():
    pt = PrettyTable(field_names= ["ID", "Married", "Divorced", "Husband_ID", "Husband_Name", "Wife_ID",
                                   "Wife_Name", "Children"])

    for i in fm.values():
        for id,married,Divorced,Husband_ID,Husband_Name,Wife_ID,Wife_Name,children in i.pt():
            pt.add_row([id,married,Divorced,Husband_ID,Husband_Name,Wife_ID,Wife_Name,children])
    print(pt)

def pt_id():
    pt = PrettyTable(field_names= ["ID","Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"])

    for i in indi.values():
        for ID,NAME,Gender,Birthday, Age, Alive, Death, Child, Spouse in i.pt():
            pt.add_row([ID,NAME,Gender,Birthday, Age, Alive, Death, Child, Spouse])
    print(pt)


def parents_not_old():
    for k, v in fm.items():
        if v.Husband_ID != 'NA' and v.Wife_ID != 'NA':
            bd_father = datetime.strptime(indi[v.Husband_ID].Birthday, '%d %b %Y')
            bd_mother = datetime.strptime(indi[v.Wife_ID].Birthday, '%d %b %Y')
            for c in v.Children:
                if indi[c].Birthday != 'NA':
                    bd_child = datetime.strptime(indi[c].Birthday, '%d %b %Y')
                    diff_father = (abs((bd_father - bd_child).days)) / 365
                    diff_mother = (abs((bd_mother - bd_child).days)) / 365
                    if diff_father > 80:
                        print('ERROR: INDIVIDUAL: US12: ' + c + ': Has over 80 years than his father which is [ ' + str(diff_father) + 'years ].')
                    if diff_mother > 60:
                        print('ERROR: INDIVIDUAL: US12: ' + c + ': Has over 60 years than his mother which is [ ' + str(diff_mother) + 'years ].')

def male_last_name():
    for k, v in fm.items():
        family_last_name = indi[v.Husband_ID].Name.split('/')[1]
        for i in v.Children:
            if indi[i].Gender == 'M' and indi[i].Name.split('/')[1] != family_last_name:
                print('ERROR: INDIVIDUAL: US16: ' + indi[i].ID + ': has last name ' + indi[i].Name.split('/')[1] +
                      ' which is different from the family last name: ' + family_last_name)

if __name__ == "__main__":
    read_person("/Users/apple/Desktop/Code/555/123.ged")
    add_infor()
    pt_fm()
    pt_id()
    parents_not_old()
    male_last_name()