from prettytable import PrettyTable
import datetime as dt
from dateFunctions import compareDates, dateBeforeCurrentDate, differenceBetweenDates, lessThan150YearsOld
from BirthBeforeMorDofParents import birthAfterMarriage_par, birthBeforeDeath_par, birthAfterMarriageOfParents, birthBeforeDeathOfParents
from BirthBeforeMorD import check_Birth_before_death, check_Birth_before_marr
from MarriageBeforeDivorce import check_marriage_before_divorce
from Marriagebeforedeath import check_marriage_before_death
from List_recent_births import list_born_in_30
from List_recent_deaths import list_died_in_30
from MaleLastName import check_male_last_name
from ParentsNotOld import check_parents_not_old
from DivorceBeforeDeath import check_divorce_before_death
from MultipleBirths import multiple_birth
from UniqueID import check_unique_id
from CorrectGender import check_correct_gender
from SiblingSpacing import check_siblingSpacing
from bigamyAndMarriageBefore14 import noBigamy, marriageAfter14
from ListUpcomingBirthdays import ListUpcomingBirthdays
from ListUpcomingAnniversaries import ListUpcomingAnniversaries
from US24 import check_unique_fm_by_spouses
from US37 import List_recent_survivors
from List_living_married import check_list_living_married
from List_living_single import listing_living_single
from US29 import listDeceased
from US34 import listLargeAgeDifferences
from lessThanFifteen import check_lessThanFifteen
from uniqueNameBday import check_uniqueNameBday
from ListMultipleBirths import listMultipleBirths
from ListOrphans import listOrphans
from us17 import NoMarrDesc
from US18 import noSiblingMarriage
from US19 import noCousinMarriage
from listAges import listAges

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
        try:
            dt.datetime.strptime(birth, '%d %b %Y')
        except:
            print(f"US42 Error: Date {birth} is not a valid date!")
            # Default date to set to not break other functions
            self.BIRT = "11 Nov 2019"
        else:
            self.BIRT = birth

    def add_deat(self, deat):
        try:
            dt.datetime.strptime(deat, '%d %b %Y')
        except:
            print(f"US42 Error: Date {deat} is not a valid date!")
            # Default date to set to not break other functions
            self.DEAT = "11 Nov 2019"
        else:
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
        if self.Alive == "False":
            dt2 = dt.datetime.strptime(self.Death, '%d %b %Y')
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
        try:
            dt.datetime.strptime(marr, '%d %b %Y')
        except:
            print(f"US42 Error: Date {marr} is not a valid date!")
            # Default date to set to not break other functions
            self.Married = "11 Nov 2019"
        else:
            self.Married = marr
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
        try:
            dt.datetime.strptime(div, '%d %b %Y')
        except:
            print(f"US42 Error: Date {div} is not a valid date!")
            # Default date to set to not break other functions
            self.Divorced = "11 Nov 2019"
        else:
            self.Divorced = div


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


pi = {}   #person information dict
indi = {}  #indiv information dict
fm = {}     #family information dic
Individual_ID_list = []  
Familiy_ID_list =[]


def read_person(path):
    fp = file_reader(path)
    
    for i in fp:
        new_i = i.split()
        if new_i[0] == "0":
            if "INDI" in new_i:
               pi[new_i[1]] = Person_info(new_i[1])
               id = new_i[1]
               Individual_ID_list.append(new_i[1])
            if "FAM" in new_i:
                fm[new_i[1]] = Families(new_i[1])
                id = new_i[1]
                Familiy_ID_list.append(new_i[1])
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



if __name__ == "__main__":
    read_person("test1.ged")
    add_infor()
    pt_id()
    pt_fm()

    # except US26,41
    dateBeforeCurrentDate(fm, indi)                     #01 --sprint 1
    check_Birth_before_marr(fm,pi)                      #02 --sprint 1
    check_Birth_before_death(indi)                      #03 --sprint 1
    check_marriage_before_divorce(fm)                   #04 --sprint 1
    check_marriage_before_death(fm,pi)                  #05 --sprint 1
    check_divorce_before_death(fm,pi)                   #06 --sprint 2
    lessThan150YearsOld(indi)                           #07 --sprint 1
    birthAfterMarriage_par(fm, pi)                      #08 --sprint 1
    birthBeforeDeath_par(fm, pi)                        #09 --sprint 1
    marriageAfter14(fm, pi)                             #10 --sprint 2
    noBigamy(fm)                                        #11 --sprint 2
    check_parents_not_old(fm,indi)                      #12 --sprint 1
    check_siblingSpacing(fm, indi)                      #13 and 28 --sprint 2
    multiple_birth(fm,pi)                               #14 --sprint 2
    check_lessThanFifteen(fm)                           #15 --sprint 3
    check_male_last_name(fm,indi)                       #16 --sprint 1
    NoMarrDesc(fm, indi)                                #17 --sprint 4
    noSiblingMarriage(fm)                               #18 --sprint 4
    noCousinMarriage(fm)                                #19 --sprint 4

    check_correct_gender(fm,indi)                       #21 --sprint 2
    check_unique_id(Individual_ID_list,Familiy_ID_list) #22 --sprint 2
    check_uniqueNameBday(pi)                            #23 --sprint 3
    check_unique_fm_by_spouses(fm)                      #24 --sprint 3

    listAges(indi)                                      #27 --sprint 4

    listDeceased(indi)                                  #29 --sprint 3
    check_list_living_married(fm,indi)                  #30 --sprint 3
    listing_living_single(indi)                         #31 --sprint 3
    listMultipleBirths(fm, pi)                          #32 --sprint 4
    listOrphans(fm,indi)                                #33 --sprint 4
    listLargeAgeDifferences(fm, indi)                   #34 --sprint 3
    list_born_in_30(indi)                               #35 --sprint 2
    list_died_in_30(indi)                               #36 --sprint 2
    List_recent_survivors(fm,indi)                      #37 --sprint 3
    ListUpcomingBirthdays(pi)                           #38 --sprint 3
    ListUpcomingAnniversaries(fm,indi)                  #39 --sprint 3