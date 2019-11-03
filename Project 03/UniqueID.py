'''
Created: 2019-10-18 10:24:42
Author : Jia Wen
Email : jwen6@stevens.edu
Description: US 22 All individual IDs should be unique and all family IDs should be unique
'''
import collections

def check_unique_id(indi_list, fm_list):

    error_ID = []

    duplicate_indi_ID = [item for item, count in collections.Counter(indi_list).items() if count > 1]
    duplicate_fm_ID = [item for item, count in collections.Counter(fm_list).items() if count > 1]

    for id in duplicate_indi_ID:
        print(f"ERROR: Individual {id} has already existed!")
        error_ID.append(id)

    for id in duplicate_fm_ID:
        print(f"ERROR: Family {id} has already existed!")
        error_ID.append(id)
    
    return error_ID




