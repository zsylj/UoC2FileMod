import os
import re
import yaml

def scene_main_mod(path):
    f=open(path,"r")
    main_content=f.read()
    temp=yaml.safe_load(main_content)
    print(temp)
    print("=======================================")
    temp["elastic_defense_units"]=[]
    temp["no_retreat_units"]=[]
    temp["rearguard_units"]=[]
    f.closed
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
            if r"\main.yml" in scene_path:
                print("F1")
                scene_main_mod(scene_path)
                print("END")

temp=UoC2(r"Unity of Command 2\_packages\dlc6\data\campaigns\desert.usc\scenarios")
