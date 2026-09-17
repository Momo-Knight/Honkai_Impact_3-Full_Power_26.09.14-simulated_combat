# Honkai_Impact_3-Full_Power_26.09.14-simulated_combat

This repository includes a python program which records all the characters' (but for Vita's, who lost before I got to know the activity) ability, and offers a simulating program for you to predict the game's result.All the abilities have been modified according to the previous games, though I am not sure whether there are not any bugs. Hope it helps.

## character.py

"character.py" provides two classes of Buff and Character. Class Buff is used to record the buffs on characters brought by their opponents, (while those provided by themselves is recorded as a variable in child classes). All the buffs is stored in character.buffList, added when the opponents use abilities, and removed when executing character.finish().

Class Character provides all the character's information and behaviors. The information includes health, attack, defense, speed and cd, but not the useless "strength". The behaviors include run(to decide what to do this round), normalAttack, activeAbility, passiveAbility and finish(to calculate some buff effects).

Their specific information and behaviors are subjectively defined in \_\_init__ and overriding functions.

## main.py

This file provides the combat logic, so the characters can battle using startGame. The \_\_main simulates their combat for 1000 times and get the result, but you can modify it according to your demandings.
