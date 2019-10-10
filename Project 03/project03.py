from prettytable import PrettyTable
import datetime as dt
from dateFunctions import compareDates, dateBeforeCurrentDate, differenceBetweenDates, lessThan150YearsOld
from BirthBeforeMorD import birth_before_death_p, birth_before_marriage_p
from MarriageBeforeDivorce import marriage_before_divorce
from Marriagebeforedeath import marriage_before_death

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


pi = {}   #person information dict
indi = {}  #indiv information dict
fm = {}     #family information dic

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


#US08	Birth before marriage of parents
def check_Birth_before_marr():
    for i in fm.values():
        # check hus birthday before marr
        hus_birthday = pi[i.Husband_ID].BIRT
        if i.Married != 'NA':
            if not birth_before_marriage_p(hus_birthday,i.Married):
                print(f'Error {i.Husband_Name} birthday_before_marr birthday{hus_birthday}  married{i.Married}')
        
        #check wife birthday before marr
        if i.Wife_ID != 'NA':
            wife_birthday = pi[i.Wife_ID].BIRT
            if not birth_before_marriage_p(wife_birthday,i.Married):
                print(f'Error {i.Wife_Name} birthday_before_marr birthday {wife_birthday}  married {i.Married}')
        

#US09	Birth before death of parents
def check_Birth_before_death():
    for i in indi.values():
        if i.Death != 'NA':
            if not birth_before_death_p(i.Birthday,i.Death):
                print(f'Error {i.Name} birthday_before_marr birthday {i.Birthday}  Death {i.Death}')

def check_marriage_before_divorce():
    for family_key in fm: # get family info
        marriage_date = fm[family_key].Married
        divorced_date = fm[family_key].Divorced 

        # convet datatime to number form
        if marriage_date != 'NA': 
            marriage_date = dt.datetime.strptime(marriage_date, '%d %b %Y')
        if divorced_date != 'NA':
            divorced_date = dt.datetime.strptime(divorced_date, '%d %b %Y')

        #check if marriage_before_divorce
        if marriage_before_divorce(marriage_date, divorced_date) == False:
            print(f'errors! family {family_key} marriage after divorce!' )

def check_marriage_before_death():
    for family_key in fm: # get family info
        family_ID = fm[family_key]
        husband_ID = family_ID.Husband_ID
        wife_ID = family_ID.Wife_ID

        # check if the ID is 'NA'
        if husband_ID != "NA":
            husband_ID = pi[family_ID.Husband_ID]
        if wife_ID != "NA":
            wife_ID = pi[family_ID.Wife_ID]

        marriage_before_death(family_ID,husband_ID,wife_ID)

if __name__ == "__main__":
    read_person("proj01.ged")
    add_infor()
    pt_id()
    pt_fm()
    check_Birth_before_marr()
    check_Birth_before_death()
    check_marriage_before_divorce()
    check_marriage_before_death()
    