import os
import re
import yaml

allied_frac=["can","ff","uk","us"]
axis_frac=["ger","hun","ita","rom","fin"]
red_frac=["sov"]

def hq_id(path,hq_id_list):
    f=open(path,"r")
    hq_content=f.read()
    temp=yaml.safe_load(hq_content)
    for item in temp:
        ind=item["template"].find("_")
        if item["template"][0:ind] in axis_frac and item["id"] not in hq_id_list:
            hq_id_list.append(item["id"])
        else:
            continue
    print(hq_id_list)
    f.closed
    return hq_id_list

#Setting Global Variable
#Make Sure the Spec can be saved via recursion
global hq_id_list
hq_id_list=[]

def UoC2(uoc_dir):
    scene_name_list=os.listdir(uoc_dir)
    for scene_name in scene_name_list:
        scene_path=os.path.join(uoc_dir,scene_name)
        print(scene_path)
        #若本文件夹内还有文件夹，调用函数
        if os.path.isdir(scene_path)==True:
            UoC2(scene_path)
        else:
            if r"\hqs.yml" in scene_path:

                print("F1")
                hq_id(scene_path,hq_id_list)
                print("END")

    print("Final")
    print(hq_id_list)
UoC2(r"F:\Steam\steamapps\common\Unity of Command 2\_packages\dlc1\data\campaigns\blitzkrieg.usc\scenarios")

def usc_main_mod(path,hq_id_list):
    f=open(path,"r")
    hq_content=f.read()
    temp=yaml.safe_load(hq_content)
    print(temp)
    temp["persistent_hqs"]=hq_id_list
    temp["prestige"]=25000
    f.closed
    with open(path,"w") as f:
        yaml.dump(temp,f)
    f.closed

usc_main_mod(r"F:\Steam\steamapps\common\Unity of Command 2\_packages\dlc1\data\campaigns\blitzkrieg.usc\main.yml",hq_id_list)
