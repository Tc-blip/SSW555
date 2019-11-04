def listDeceased(indi):
    deadIDs = []
    for key in indi:
        individual = indi[key]
        if individual.Alive == "False":
            print("US29: Individual " + individual.ID + " is dead.")
            deadIDs.append(individual.ID)
    return deadIDs
