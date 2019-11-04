'''
Created: 2019-10-24 17:56:48
Author : Jia Wen
Email : jwen6@stevens.edu
Description: US 31 List all living and over 30-year-old people who have never been married.
'''
import datetime as dt

def listing_living_single(indi):

    dt_now = dt.datetime.now()
    for k,v in indi.items():
        dt_birth = dt.datetime.strptime(indi[k].Birthday, '%d %b %Y')
        if abs(dt_now - dt_birth).days > 30:
            if check_living_single(indi[k].Death, indi[k].Spouse) == True:
                print(f"Individual {k}, over 30 years old and alive, has never been married.")

def check_living_single(death,spouse):
    if death == "NA" and spouse == []:
        return True
    else:
        return False