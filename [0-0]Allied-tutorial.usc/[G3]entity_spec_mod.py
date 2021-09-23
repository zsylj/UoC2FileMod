import os
import re
import yaml

def unit_spec(path,uk_spec_list,us_spec_list):
    f=open(path,"r")
    unit_content=f.read()
    temp=yaml.safe_load(unit_content)
    for item in temp:
        if item["specs"]!=[]:
            for item2 in item["specs"]:
                ind=item2["type"].find("_")
                if item2["type"][0:ind]=="uk" and item2["type"] not in uk_spec_list:
                    uk_spec_list.append(item2["type"])
                elif item2["type"][0:ind]=="us" and item2["type"] not in us_spec_list:
                    us_spec_list.append(item2["type"])
                else:
                    continue
        else:
            continue
    print(uk_spec_list)
    print(us_spec_list)
    f.closed
    return uk_spec_list,us_spec_list

def enroute_spec(path,uk_spec_list,us_spec_list):
    f=open(path,"r")
    enroute_content=f.read()
    temp=yaml.safe_load(enroute_content)
    for item in temp:
        if item["unit"]["specs"]!=[]:
            for item2 in item["unit"]["specs"]:
                ind=item2["type"].find("_")
                if item2["type"][0:ind]=="uk" and item2["type"] not in uk_spec_list:
                    uk_spec_list.append(item2["type"])
                elif item2["type"][0:ind]=="us" and item2["type"] not in us_spec_list:
                    us_spec_list.append(item2["type"])
                else:
                    continue
        else:
            continue
    print(uk_spec_list)
    print(us_spec_list)
    f.closed
    return uk_spec_list,us_spec_list

#Setting Global Variable
#Make Sure the Spec can be saved via recursion
global uk_spec_list
global us_spec_list
uk_spec_list=[]
us_spec_list=[]

def UoC2(uoc_dir):
    scene_name_list=os.listdir(uoc_dir)
    for scene_name in scene_name_list:
        scene_path=os.path.join(uoc_dir,scene_name)
        print(scene_path)
        #若本文件夹内还有文件夹，调用函数
        if os.path.isdir(scene_path)==True:
            UoC2(scene_path)
        else:
            if r"\units.yml" in scene_path:

                print("F1")
                unit_spec(scene_path,uk_spec_list,us_spec_list)
                print("END")
                
            elif r"\enroute_units.yml" in scene_path:
                print("F2")
                enroute_spec(scene_path,uk_spec_list,us_spec_list)
                print("END")

    print("UK_Final")
    print(uk_spec_list)
    print("US_Final")
    print(us_spec_list)
UoC2(r"_packages\base\data\campaigns\tutorial.usc\scenarios")#####


def spec_mod(path,uk_spec_list,us_spec_list):
    for item in uk_spec_list:
        new_path=path+item+".yml"
        f=open(new_path,"r")
        spec_content=f.read()
        temp=yaml.safe_load(spec_content)
        #print(temp)
        temp["attack"]=100
        temp["defense"]=100
        temp["armor"]=100
        temp["artillery"]=100
        temp["att_idx"]=10
        temp["dfe_idx"]=10
        temp["flags"]=["arty", "at", "engineers", "lci", "recon", "special"]
        f.closed
        with open(new_path,"w") as f:
            yaml.dump(temp,f)
        f.closed

    for item in us_spec_list:
        new_path=path+item+".yml"
        f=open(new_path,"r")
        spec_content=f.read()
        temp=yaml.safe_load(spec_content)
        #print(temp)
        temp["attack"]=100
        temp["defense"]=100
        temp["armor"]=100
        temp["artillery"]=100
        temp["att_idx"]=10
        temp["dfe_idx"]=10
        temp["flags"]=["arty", "at", "engineers", "lci", "recon", "special"]
        f.closed
        with open(new_path,"w") as f:
            yaml.dump(temp,f)
        f.closed

spec_mod(r"_packages/base/data/entity_types/specialists/",uk_spec_list,us_spec_list)
