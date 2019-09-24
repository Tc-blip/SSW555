from prettytable import PrettyTable

class Individuals:
    __slots__ = ["ID","Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    def __init__(self,id,name,gen,bday,age,alive,death,child,spouse):
        self.ID = id
        self.Name = name
        self.Gender = gen
        self.Birthday = bday
        self.Age = age
        self.Alive = alive
        self.Death = death
        self.Child = child
        self.Spouse = spouse

    


class Families:
    __slots__ = ["ID", "Married", "Divorced", "Husband_ID", "Husband_Name", "Wife_ID", 
    "Wife_Name", "Children"]
    def __init__(self, id ,marr,div,hus_id, hus_name, wife_id, wife_name, child):
        self.ID = id
        self.Married = marr
        self.Divorced = div
        self.Husband_ID = hus_id
        self. Husband_Name = hus_name
        self.Wife_ID = wife_id
        self.Wife_Name = wife_name
        self.Children = child

