from prettytable import PrettyTable

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
        self.Child = "NA"
        self.Spouse = "NA"
    

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
    def add_husb(self,husb):
        self.Husband_ID = husb
    def add_wife(self,wife):
        self.Wife_ID = wife
    def add_chil(self,chil):
        self.Children.append(chil)
    def add_div(self,div):
        self.Divorced = div

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
        
           
if __name__ == "__main__":
    read_person("test.ged")
    
