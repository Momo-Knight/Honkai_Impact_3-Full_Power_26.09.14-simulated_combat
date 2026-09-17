from character import *

class 芽衣(Character):
    def __init__(self):
        super().__init__()
        self.name = "芽衣"
        self.health = 100
        self.attack = 18
        self.defense = 8
        self.speed = 24

        self.abilityCD = 1
        self.activeTimer = 1

    刀势 = 0

    def activeAbility(self, other: Character, config):
        if self.刀势 >= 2:
            # 强化战技
            self.normalAttack(other, 25)
            self.trueAttack(other, 8)
            print("    芽衣：强化掏心窝子！")
            self.刀势 = 0
        else:
            # 普通战技
            self.normalAttack(other, 15)
            if random() <= 5:
                other.health -= 4
                print("    芽衣：掏心窝子！")
        if random() <= 40:
            self.刀势 += 1
        else:
            self.刀势 += 2

    def trueAttack(self, other, attack):
        if other.name == "幽兰黛尔" or other.name == "布洛妮娅":
            whole = other.health + other.armer
            whole -= max(attack, 0)
            if whole < other.health:
                other.health = whole
                other.armer = 0
            else:
                other.armer = whole - other.health
        else:
            other.health -= max(attack, 0)
        if other.name == "希儿":
            other.passiveAbility(self, 0)
        return True

    def print(self):
        print(self.name, end="   ")
        defense = str(self.defense) + self.丽塔_防御降低3 * "-3" + bool(self.游云_防御降低) * f"-{self.游云_防御降低}"
        print(f"{self.health} a={self.attack} d={defense} cd={self.activeTimer} 刀势={self.刀势}")