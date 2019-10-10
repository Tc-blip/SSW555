#Project02
#Cheng Tian

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


tag_0 =  {'HEAD', 'TRLR', 'NOTE', 'INDI', 'FAM'}
tag_1 = {'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV'}
tag_2 = {'DATE'}

def convert_0(new_ged):
    if len(new_ged) < 3:
        if new_ged[1] in tag_0:
            return [new_ged[0],new_ged[1],"Y"]
        else:
            return [new_ged[0],new_ged[1],"N"]
    else:
        if new_ged[2] in tag_0:
            return [new_ged[0],new_ged[2],"Y",new_ged[1]]
        elif new_ged [1] in tag_0:
            return [new_ged[0],new_ged[1],"Y"," ".join(new_ged[2:])]
        else:
            return [new_ged[0],new_ged[1],"N"," ".join(new_ged[2:])]

def convert_1(new_ged):
    if new_ged [1] in tag_1:
        return [new_ged[0],new_ged[1],"Y"," ".join(new_ged[2:])]
    else:
        return [new_ged[0],new_ged[1],"N"," ".join(new_ged[2:])]

def convert_2(new_ged):
    if new_ged [1] in tag_1:
        return [new_ged[0],new_ged[1],"Y"," ".join(new_ged[2:])]
    else:
        return [new_ged[0],new_ged[1],"N"," ".join(new_ged[2:])]

def convert(ged_line):
    new_ged = ged_line.split()
    res = []
    if new_ged[0] == "0":
        res = convert_0(new_ged)
    elif new_ged[0] == "1":
        res = convert_1(new_ged)
    elif new_ged[0] == "2":
        res = convert_2(new_ged)

    return "|".join(res)
         

if __name__ == "__main__":
    wudi = file_reader("Project01.ged")
    for i in wudi:
        print("-->" + i)
        print("<--" + convert(i))

    

