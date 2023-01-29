import os
import re
import yaml

def nation_mod(path):
    f=open(path,"r")
    nation_content=f.read()
    temp=yaml.safe_load(nation_content)
    for item in temp:
        print(item)
        print(temp[item])
        print("===========================")
    temp["finnish"].update({'parent_nationality': 'german'})
    temp["spanish"].update({'parent_nationality': 'german'})
    temp["estonian"].update({'parent_nationality': 'german'})
    f.closed
    with open(path,"w") as f:
        yaml.dump(temp,f)
    f.closed

nation_mod(r"Unity of Command 2\_packages\base\data\entity_types\nationalities.yml")
