import os
import re
import yaml

def config_mod(path):
    f=open(path,"r")
    config_content=f.read()
    temp=yaml.safe_load(config_content)
    for item in temp:
        print(item)
        print(temp[item])
        print("===========================")
    temp["earned_experience"]=[20, 10, 5, 1]
    temp["att_loss_table"]["easy"]=[5, 4, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    temp["att_loss_table"]["normal"]=[5, 4, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    temp["att_loss_table"]["classic"]=[5, 4, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    temp["att_loss_table"]["hard"]=[5, 4, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    temp["att_loss_table_p2"]=[5, 4, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    temp["dfe_loss_table"]=[0, 0, 0, 1, 7, 7, 7, 7, 7, 7, 7, 7, 7]
    temp["dfe_sup_table"]=[0, 0, 0, 1, 7, 7, 7, 7, 7, 7, 7, 7, 7]
    temp["retreat_table"]=[0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    temp["overrun_table"]=[0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    temp["att_k0_no_overrun"]=[0, 1, 1]
    temp["att_k0_overrun"]=[1, 1, 2]
    temp["combat_city_ruin_chance"]=1.0
    f.closed
    with open(path,"w") as f:
        yaml.dump(temp,f)
    f.closed

config_mod(r"_packages\base\config\game.yml")
