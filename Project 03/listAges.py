# US27 Include Individual Ages
# Include person's current age when listing individuals

def listAges(indi):
    for i in indi:
        info = indi[i]
        print(f"US27: {info.Name} is currently {info.Age} years old.")