import os
import re
import yaml

def bridge_mod(path):
    f=open(path,"r")
    bridge_content=f.read()
    temp=yaml.safe_load(bridge_content)
    try:
        del temp["map"]
    except KeyError:
        print("Bridges.yml Do Not Contain Key['map'] i.e. This scene do not have broken bridge")
    try:
        for item in temp["gamelike"]:
            #print(item)
            item[1]["in_build"]=False
    except KeyError:
        print("Bridges.yml Do Not Contain Key['gamelike'] i.e. This scene do not have floating bridge")
    f.closed
    with open(path,"w") as f:
        yaml.dump(temp,f)
    f.closed

def fort_mod(path):
    f=open(path,"r")
    fort_content=f.read()
    temp=yaml.safe_load(fort_content)
    #print(temp)
    #print("=======================================")
    for item in temp["map"]:
        item[1]["functional"]=False
        #print(item)
    f.closed
    #print(temp)
    with open(path,"w") as f:
        yaml.dump(temp,f)
    f.closed

def UoC2(uoc_dir):
    scene_name_list=os.listdir(uoc_dir)
    for scene_name in scene_name_list:
        scene_path=os.path.join(uoc_dir,scene_name)
        print(scene_path)
        #若本文件夹内还有文件夹，调用函数
        if os.path.isdir(scene_path)==True:
            UoC2(scene_path)
        else:
            if r"\bridges.yml" in scene_path:

                print("F1")
                bridge_mod(scene_path)
                print("END")
                
            elif r"\forts.yml" in scene_path:
                print("F2")
                fort_mod(scene_path)
                print("END")

temp=UoC2(r"F:\Steam\steamapps\common\Unity of Command 2\_packages\base\data\campaigns\france.usc\scenarios")
