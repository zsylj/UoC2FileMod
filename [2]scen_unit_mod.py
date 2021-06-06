import os
import re
import yaml

#Look up table
def lut(path):
    f=open(path,"r")
    temp_all=f.read()
    temp_list=temp_all.split("\n")
    pair_list=[item for item in temp_list if "name" not in item]
    del pair_list[-1]

    #读取本DLC中所有涉及到的Unit ID
    id_list=[pair_list[i][6::] for i in range(0,len(pair_list),2)]
    #print(len(id_list))
    #print(id_list)

    #读取本DLC中所有涉及到的Unit Type
    type_list=[pair_list[i][8::] for i in range(1,len(pair_list),2)]
    #print(len(type_list))
    #print(type_list)

    #对Unit Type的前部分国家代码进行记录
    country_list=[]
    for item in type_list:
        ind=item.find("_")#头部国家代码定位
        country_list.append(item[0:ind])
    #print(country_list)

    #对Unit Type的头和尾进行切除，保留中间Type缩写
    pattern_tail=r"_[34][0123459]_?[0-2]?"#去掉尾部年份及分支标识
    s_type_list=[]
    for item in type_list:
        ind=item.find("_")
        item=item[ind+1::]
        item=re.sub(pattern_tail,"",item)
        s_type_list.append(item)
        #print(item)
    #print(s_type_list)

    #对国家代码进行装备购买划分（基于parent划分）
    #苏、德、美、英、UNK
    #UNK意味着不可购买兵牌国家，例如芬兰、爱沙尼亚等
    parent_list=[]
    sov_parent=["sov"]
    ger_parent=["ger","ss","cro","hun","ita","rom","rsi","svk","vf"]
    us_parent=["us","bra","ff"]
    uk_parent=["uk","aus","can","gr","ind","nor","nz","pol","sa","yug"]
    no_parent=["bel","bul","est","fin","fr","nl","spa","swe","sws"]
    for item in country_list:
        if item=="sov":
            parent_list.append("sov")
        elif item in ger_parent:
            parent_list.append("ger")
        elif item in us_parent:
            parent_list.append("us")
        elif item in uk_parent:
            parent_list.append("uk")
        else:
            parent_list.append("UNK")
    #print(parent_list)

    #将Unit分为步兵和非步兵，以便修改兵牌
    #步兵携带兵牌：工兵、榴弹炮、88炮
    #非步兵携带兵牌：232侦察车、三号突击炮B、二号坦克
    gen_type=[]
    mot_list=["cav","mot","mech","mrd","arm","dlm","lehr","pz","pzgr","tank","arm_cc"]
    for item in s_type_list:
        if item in mot_list:
            gen_type.append("type2")
        else:
            gen_type.append("type1")
    #print(gen_type)
    
    f.closed
    return id_list,country_list,s_type_list,parent_list,gen_type

id_list,country_list,s_type_list,parent_list,gen_type=lut("D:/Program Files/Steam/steamapps/common/Unity of Command 2/_packages/dlc2/data/campaigns/barbarossa.usc/units.yml")

#unit_segment
def unit_sgmnt(path):
    f=open(path,"r")
    unit_content=f.read()
    temp=yaml.safe_load(unit_content)
    for item in temp:
        ind=id_list.index(str(item["id"]))
        if parent_list[ind]=="ger":
            item["act_st"]=7
            item["xp"]=300
            if gen_type[ind]=="type1":
                item["specs"]=[{'active': True, 'captured': False, 'idx': 0, 'type': 'ger_eng_42'}, {'active': True, 'captured': False, 'idx': 1, 'type': 'ger_towed_arty_42'}, {'active': True, 'captured': False, 'idx': 2, 'type': 'ger_towed_at_42'}]
            else:
                item["specs"]=[{'active': True, 'captured': False, 'idx': 0, 'type': 'ger_asg_41'}, {'active': True, 'captured': False, 'idx': 1, 'type': 'ger_pzx_40'}, {'active': True, 'captured': False, 'idx': 2, 'type': 'ger_recon_41'}]
        elif parent_list[ind]=="sov":
            item["act_st"]=1
            item["entr"]=0
            item["specs"]=[]
            item["xp"]=0
    f.closed
    with open(path,"w") as f:
        yaml.dump(temp,f)
    f.closed
    #for item in temp:
    #    print(item)

#unit_sgmnt(r"D:\Program Files\Steam\steamapps\common\Unity of Command 2\_packages\dlc2\data\campaigns\barbarossa.usc\scenarios\bryansk\units.yml")

#enroute_segment
def enroute_sgmnt(path):
    f=open(path,"r")
    enroute_content=f.read()
    temp=yaml.safe_load(enroute_content)
    for item in temp:
        #print(item["unit"])
        ind=id_list.index(str(item["unit"]["id"]))
        if parent_list[ind]=="ger":
            item["unit"]["act_st"]=7
            item["unit"]["xp"]=300
            if gen_type[ind]=="type1":
                item["unit"]["specs"]=[{'active': True, 'captured': False, 'idx': 0, 'type': 'ger_eng_42'}, {'active': True, 'captured': False, 'idx': 1, 'type': 'ger_towed_arty_42'}, {'active': True, 'captured': False, 'idx': 2, 'type': 'ger_towed_at_42'}]
            else:
                item["unit"]["specs"]=[{'active': True, 'captured': False, 'idx': 0, 'type': 'ger_asg_41'}, {'active': True, 'captured': False, 'idx': 1, 'type': 'ger_pzx_40'}, {'active': True, 'captured': False, 'idx': 2, 'type': 'ger_recon_41'}]
        #print(item)
    f.closed
    with open(path,"w") as f:
        yaml.dump(temp,f)
    f.closed

#enroute_sgmnt(r"D:\Program Files\Steam\steamapps\common\Unity of Command 2\_packages\dlc2\data\campaigns\barbarossa.usc\scenarios\bryansk\enroute_units.yml")

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
                unit_sgmnt(scene_path)
                print("END")
                
            elif r"\enroute_units.yml" in scene_path:
                print("F2")
                enroute_sgmnt(scene_path)
                print("END")

temp=UoC2(r"D:\Program Files\Steam\steamapps\common\Unity of Command 2\_packages\dlc2\data\campaigns\barbarossa.usc\scenarios")





