import os
import re
import yaml

allied_frac=["can","ff","uk","us"]
axis_frac=["ger","hun","ita","rom","fin"]
red_frac=["sov"]

def hq(path,hq_list):
    f=open(path,"r")
    hq_content=f.read()
    temp=yaml.safe_load(hq_content)
    for item in temp:
        ind=item["template"].find("_")
        if item["template"][0:ind] in allied_frac and item["template"] not in hq_list:
            hq_list.append(item["template"])
        else:
            continue
    print(hq_list)
    f.closed
    return hq_list

#Setting Global Variable
#Make Sure the Spec can be saved via recursion
global hq_list
hq_list=[]

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
                hq(scene_path,hq_list)
                print("END")
    print("Final")
    print(hq_list)
UoC2(r"Unity of Command 2\_packages\dlc6\data\campaigns\desert.usc\scenarios")

def hq_mod(path,hq_list):
    for item in hq_list:
        new_path=path+item+".yml"
        f=open(new_path,"r")
        hq_content=f.read()
        temp=yaml.safe_load(hq_content)
        print(temp)
        for item2 in temp["branches"]:
            print(item2)
            for item3 in temp["branches"][item2]:
                print(item3)
                item3["cost"]=1
        temp["fp_max_steps"]=1000000
        temp["max_cp"]=9
        temp["trucks"]=5
        #个别hq没有init_levels键
        try:
            for item4 in temp["init_levels"]:
                temp["init_levels"][item4]=3
        except KeyError:
            temp.update({'init_levels': {'engineering': 3, 'force_pool': 3, 'intel': 3, 'logistics': 3, 'operations': 3}})
        #个别hq没有fixed_movement键
        try:
            temp["fixed_movement"]=100#
        except KeyError:
            temp.update({'fixed_movement': 100})
        #个别hq没有fixed_range键
        try:
            temp["fixed_range"]=100#
        except KeyError:
            temp.update({'fixed_range': 100})
        f.closed
        
        hq_check_list=["can_hq","ff_hq","ger_hq","hun_hq","ita_hq","uk_hq","us_hq","vichy_hq"]
        if item not in hq_check_list:
            with open(new_path,"w") as f:
                yaml.dump(temp,f)
            f.closed
        else:
            #save basic
            with open(new_path,"w") as f:
                yaml.dump(temp,f)
            f.closed
            #save sub
            difficulties_list=["easy","normal","classic","hard"]
            history_intervals_list=["early","mid","late"]
            for item_hist in history_intervals_list:
                for item_diff in difficulties_list:
                    new_path2=path+item+"_"+item_hist+"_"+item_diff+".yml"
                    with open(new_path2,"w") as f:
                        yaml.dump(temp,f)
                    f.closed
        
hq_mod(r"Unity of Command 2/_packages/base/data/entity_types/hq_types/",hq_list)
