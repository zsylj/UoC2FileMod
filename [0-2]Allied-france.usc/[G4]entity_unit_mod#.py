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

    #将Unit Type进行阵营分割
    #红色阵营、盟军阵营、轴心阵营
    faction_list=[]
    red_fac=["sov"]
    allied_fac=["us","bra","ff","uk","aus","can","gr","ind","nor","nz","pol","sa","yug","bel","fr","nl","swe","sws"]
    axis_fac=["ger","ss","cro","hun","ita","rom","rsi","svk","vf","bul","est","fin","spa"]
    for item in country_list:
        if item in red_fac:
            faction_list.append("red")
        elif item in allied_fac:
            faction_list.append("allied")
        else:
            faction_list.append("axis")
    #print(faction_list)

    #去重复的Unit Type列表
    rr_type_list=[]
    for item in type_list:
        ind=item.find("_")
        if item[0:ind] in allied_fac:##############
            if item in rr_type_list:
                continue
            else:
                rr_type_list.append(item)
        else:
            continue
    print(rr_type_list)
        
    f.closed
    return id_list,country_list,faction_list,rr_type_list

id_list,country_list,faction_list,rr_type_list=lut(r"_packages/base/data/campaigns/france.usc/units.yml")#################

#
def unit_mod(path,rr_type_list):
    for item in rr_type_list:
        new_path=path+item+".yml"
        f=open(new_path,"r")
        unit_content=f.read()
        temp=yaml.safe_load(unit_content)
        temp["move"]=100
        temp["xmove"]=100
        temp["attack"]=100
        temp["defense"]=100
        temp["armor"]=100
        temp["max_st"]=7
        temp["max_spec"]=3
        #print(temp)
        f.closed
        with open(new_path,"w") as f:
            yaml.dump(temp,f)
        f.closed

unit_mod(r"_packages/base/data/entity_types/unit_types/",rr_type_list)
