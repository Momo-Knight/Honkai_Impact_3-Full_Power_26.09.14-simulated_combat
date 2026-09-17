import 科拉莉
from 寻梦者 import *
from 丽塔 import *
from 幽兰黛尔 import *
from 琪亚娜 import *
from 科拉莉 import *
from 芽衣 import *
from 布洛妮娅 import *
from 赫丽娅 import *
from 游云 import *
from 希儿 import *
from 希娜狄雅 import *

def startGame(A : Character, B : Character):
    print("===比赛开始===")
    characterList = [A, B]
    if A.speed > B.speed:
        on = False
    elif A.speed < B.speed:
        on = True
    else:
        on = False
        print(f"[WARNING] {A.name} 和 {B.name} 的速度相同")
    first = on

    round = 0
    while True:
        if on == first:
            round += 1
        print(f"当前回合：{round}")
        X = characterList[on]
        Y = characterList[not on]
        X.run(Y)

        X.finish(Y)

        if A.health <= 0:
            print(f"{B.name} 胜利\n")
            return 1
        if B.health <= 0:
            print(f"胜利 {A.name}\n")
            return 0

        on = not on

        X.print()
        Y.print()
        print("")

        if round >= 100:
            print("[WARNING} 回合数过多，已终止\n")
            return -1

if __name__ == '__main__':
    score = [0, 0]
    for i in range(1000):
        team = [布洛妮娅(), 希儿()]
        result = startGame(team[0], team[1])
        if result == 0 or result == 1:
            score[result] += 1
    print(f"{team[0].name} : {team[1].name} = {score[0]} : {score[1]}")