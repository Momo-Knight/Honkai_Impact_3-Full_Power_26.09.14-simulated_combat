from character import *

class 布洛妮娅(Character):
    分裂屏障 = 0
    armer = 0

    def __init__(self):
        super().__init__()
        self.name = "布洛妮娅"
        self.health = 100
        self.attack = 16
        self.defense = 8
        self.speed = 23

        self.abilityCD = 3
        self.activeTimer = 3

    def activeAbility(self, other : Character, config):
        print("    布洛妮娅，屏障展开！")
        from random import randint
        num = randint(4, 10)
        self.armer += num
        print(f"    然后获得了{num}点护盾")
        self.分裂屏障 = 2
        self.normalAttack(other)

    def normalAttack(self, other : Character, attack = -1):
        # 问题在于这个两次伤害对希儿被动算几次
        # 我目测是1次
        super().normalAttack(other, attack)
        if self.分裂屏障 > 0:
            if other.name != "希儿":
                super().normalAttack(other, attack)
            else:
                defense = other.defense - other.游云_防御降低
                if other.丽塔_防御降低3:
                    defense -= 3
                if attack == -1:
                    attack = self.attack
                other.health -= max(attack - defense, 0)
                return True

    def finish(self, other : Character):
        super().finish(other)
        self.分裂屏障 -= 1

    def print(self):
        print(self.name, end="   ")
        defense = str(self.defense) + self.丽塔_防御降低3 * "-3" + bool(self.游云_防御降低) * f"-{self.游云_防御降低}"
        print(f"{self.health}+{self.armer} a={self.attack} d={defense} cd={self.activeTimer} 分裂屏障={max(self.分裂屏障, 0)}")