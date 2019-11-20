"""
Chih-Yu Lee
US32
List multiple births
List all multiple births in a GEDCOM file
"""
def listMultipleBirths(fm,pi):
    multiple_births = []
    for key in fm:
        fm_multi_bith = []
        fmID = key
        fm_cild = fm[key].Children

        if not fm_cild:
            continue
        else:
            fm_child_bith_dict = {}
            for child in fm_cild:
                if not pi[child].BIRT in fm_child_bith_dict:
                    fm_child_bith_dict[pi[child].BIRT] = [child]
                else:
                    fm_child_bith_dict[pi[child].BIRT].append(child)
        for key, value in fm_child_bith_dict.items():
            if len(value)>=2:
                fm_multi_bith.append([key,value])
                multiple_births.append([key,value])
                print(f'US32: FAMILY: {fmID} has multiple_births list:{fm_multi_bith}')
      
    return multiple_births




