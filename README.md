# 崩坏3 火力全开！银河梦幻擂台！（26.09.14） 模拟战斗

这个仓库里有一个 Python 程序，记录了所有角色的技能（除了薇塔），还带一个模拟程序，帮你预测对局结果。所有技能都根据之前的对局做了调整，不过我不确定还有没有 bug。希望能帮上忙。

## character.py

`character.py` 提供了 Buff 和 Character 两个类。Buff 类用来记录对手给角色挂上的 buff（角色自身提供的 buff 则作为子类里的一个变量记录）。所有 buff 都存在 `character.buffList` 里，对手用技能时加进去，角色执行 `character.finish()` 时再移除。

Character 类则包含角色的全部信息和行为。信息包括生命值、攻击、防御、速度和 cd，除了非常有用的“战力”。行为包括 run（决定这回合干啥）、normalAttack、activeAbility、passiveAbility 和 finish（结算一些效果）。

它们的具体信息和行为都分别在 `__init__` 和重写函数里定义。

## main.py

这个文件负责战斗逻辑，所以角色可以用 `startGame` 来对战。`__main__` 会把战斗模拟 1000 次并输出结果，你也可以按自己的需求改。


# Honkai_Impact_3-Full_Power_26.09.14-simulated_combat

This repository includes a python program which records all the characters' (but for Vita's, who lost before I got to know the activity) ability, and offers a simulating program for you to predict the game's result.All the abilities have been modified according to the previous games, though I am not sure whether there are not any bugs. Hope it helps.

## character.py

"character.py" provides two classes of Buff and Character. Class Buff is used to record the buffs on characters brought by their opponents, (while those provided by themselves is recorded as a variable in child classes). All the buffs is stored in character.buffList, added when the opponents use abilities, and removed when executing character.finish().

Class Character provides all the character's information and behaviors. The information includes health, attack, defense, speed and cd, but not the useless "strength". The behaviors include run(to decide what to do this round), normalAttack, activeAbility, passiveAbility and finish(to calculate some buff effects).

Their specific information and behaviors are subjectively defined in \_\_init__ and overriding functions.

## main.py

This file provides the combat logic, so the characters can battle using startGame. The \_\_main__ simulates their combat for 1000 times and get the result, but you can modify it according to your demandings.
