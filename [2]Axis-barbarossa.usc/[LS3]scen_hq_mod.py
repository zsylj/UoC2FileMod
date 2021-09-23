import os
import re
import yaml

allied_frac=["can","ff","uk","us"]
axis_frac=["ger","hun","ita","rom","fin"]
red_frac=["sov"]

def scene_hq_mod(path):
    f=open(path,"r")
    hq_content=f.read()
    temp=yaml.safe_load(hq_content)
    #print(temp)
    for item in temp:
        print(item)
        print("=====================")
        ind=item["template"].find("_")
        if item["template"][0:ind] in axis_frac:
            for item2 in item["branch_levels"]:
                print(item2)
                item["branch_levels"][item2]["level"]=3
            for item3 in item["branches"]:
                print(item3)
                for item4 in item["branches"][item3]:
                    print(item4)
                    item4["cost"]=1
            item["fixed_movement"]=100#
            item["fixed_range"]=100#
            item["max_cp"]=9
            item["persistent"]=True
            item["trucks"]=5
        else:
            continue
    f.closed
    with open(path,"w") as f:
        yaml.dump(temp,f)
    f.closed

#scene_hq_mod(r"F:\Steam\steamapps\common\Unity of Command 2\_packages\dlc2\data\campaigns\barbarossa.usc\scenarios\hgs\hqs.yml")

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
                scene_hq_mod(scene_path)
                print("END")

UoC2(r"F:\Steam\steamapps\common\Unity of Command 2\_packages\dlc2\data\campaigns\barbarossa.usc\scenarios")
