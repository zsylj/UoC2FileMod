# UoC2FileMod
"Unity of Command Ⅱ" file modify codes

“统一指挥Ⅱ” 文件修改程序

========================================================================

IMPORTANT NOTICE 1: CODES CANNOT BE EXECUTED ACROSS FILE FOLDERS(DLCs)

注意1：不要跨文件夹运行代码

IMPORTANT NOTICE 2: ALWAYS RESTORE OFFICIAL UOC2 FILE BEFORE EXECUTING CODES IN ONE FOLDER

注意2：运行一个文件夹内的代码前，务必复原所有游戏文件

To restore official UoC2 files, go to:

https://help.steampowered.com/en/faqs/view/0C48-FCBD-DA71-93EB

复原游戏文件请参考：

https://help.steampowered.com/zh-cn/faqs/view/0C48-FCBD-DA71-93EB

========================================================================

Q01: What are these codes doing?

问01：这些代码在干什么？

A01: These codes can significantly reduce the gameplay difficulties.

答01：这些代码可以大幅降低游戏难度

Q02: How to run these codes?

问02：这些代码该如何运行？

A02: First, make sure you put them correctly in your local UoC2 file folder. Then run them in current order. zsylj has already put those codes in order, [G0]→[G1]→[G2]→[G3]→[G4]→[G5]→[LG1]→[LG2]→[LS1]→[LS2]→[LS3]→[LS4].

答：首先确保你的代码已经放在了正确的本地UoC2文件夹中。然后按顺序运行即可。zsylj已经按照顺序将他们排好了， [G0]→[G1]→[G2]→[G3]→[G4]→[G5]→[LG1]→[LG2]→[LS1]→[LS2]→[LS3]→[LS4].

Q03: What are those prefix [G0], [LG1], [LS] menas?

问03：名称中的那些前缀 [G], [LG], [LS] 都意味着什么？

A03: It deeply connect to the game file system. [G] menas globally, run these codes will cause global change (changes happens in every DLC). [LG] means locally global, run these codes will cause global change in DLC (changes only happens in specific DLC). [LS] means locally scenario, run these codes will cause locally change in scenario (changes only happens in specific scenario).

答03：这和文件系统深度相关。 [G] 意味着做出全局改变，运行这些代码将对全局设定做出改变（每个DLC都会有改变）。 [LG] 意味着对特定DLC做出全局改变，运行这些代码将对特定DLC做出全局改变。 [LS] 意味着做出局部场景改变，运行这些代码仅能对特定场景做出改变。

Q04: Instead of running the whole folder, can I run part of the codes?

问04：相对于运行整个文件夹的代码，我可以只运行部分代码吗？

A04: Yes you can, but zsylj do not recommend doing like this. Because these codes are connected. For example, if you run [scen_unit_mod.py] without running [scen_main_mod.py] definitely will occur a Error, Because [scen_unit_mod.py] set enemy active steps to 0 and [scen_main_mod.py] remove all enemy rearguard and elastic_defense buffs and those buff need at least one active step!

答04：可以，但是zsylj并不建议你这么做，因为代码都是相关联的。举个例子，如果你运行了[scen_unit_mod.py]却没有运行[scen_main_mod.py]，肯定会导致游戏报错，因为[scen_unit_mod.py]将敌人活跃战力置0，而[scen_main_mod.py]移除敌人弹性防御和后卫部队的buff，这些buff需要至少一个活跃战力。

========================================================================

P.S. [G0] and [G5] are all the same, to make the code easy to use, zsylj has duplicate them in every folder.

附 [G0] 和 [G5] 完全一致，只是出于方便用户使用的原因，zsylj将它们复制粘贴到了每一个文件夹内

P.S. [G1] should be the card modification, since we have the [LG1]usc_mian_mod.py that can add prestige up to 25000, it is useless to modify the card anymore.

附 [G1]按计划是卡牌修改，但是由于 [LG1]usc_mian_mod.py 中已经将声望修改到了25000，所以修改卡牌就没有必要了。

P.S. [G5] only works in barbarossa.usc adding [parent nationality] [German] to [Finland] and [Estonia] (this means Finland & Estonia now can buy German specialists)_

附 [G5] 只会在巴巴罗萨DLC中起到作用，它在芬兰、爱沙尼亚的国家性质中增加了装备来源国：德国（也就是说芬兰和爱沙尼亚可以购买并携带德国特种战力了）

=======================================================================

|country_name_brief_prefix|country_name_full|Chinese|
|----|----|----|
|bel|Belgium|比利时王国|
|can|Canada|加拿大|
|ff|Free_France|自由法国|
|fin|Finland|芬兰共和国|
|fr|France|法兰西第三共和国|
|ger|Germany|德意志帝国|
|gr|Greece|希腊共和国|
|hun|Hungary|匈牙利王国|
|ita|Italy|意大利王国|
|nl|Netherlands|荷兰王国|
|nr|Norway|挪威王国|
|pol|Poland|波兰第二共和国|
|rom|Romania|罗马尼亚王国|
|rsi|Repubblica Sociale Italiana|意大利社会共和国|
|sov|Soviet|苏维埃社会主义共和国联盟|
|swe|Sweden|瑞典王国|
|sws|Swiss|瑞士联邦|
|uk|United Kingdom|大不列颠及北爱尔兰联合王国|
|us|United States|美利坚合众国|
|vf/vichy|Vichy France|维希法国|
|yug|Yugoslavia|南斯拉夫王国|
