from character import *

class 赫丽娅(Character):
    def __init__(self):
        super().__init__()
        self.name = "赫丽娅"
        self.health = 100
        self.attack = 20
        self.defense = 9
        self.speed = 22

        self.abilityCD = 3
        self.activeTimer = 3

    灼光 = 0

    def activeAbility(self, other : Character, config):
        print("    苍龙灼世")
        super().normalAttack(other, 22)
        self.灼光 += 1
        if random() <= 25:
            other.buffList.append(眩晕(other, 2))
            print("    这个赫丽娅有些肉麻")

    def normalAttack(self, other : Character, attack = -1):
        if attack == -1:
            attack = self.attack
        defense = other.defense - other.游云_防御降低
        if other.丽塔_防御降低3:
            defense -= 3
        damage = max(attack - defense, 0)
        # 判定灼光增伤
        if self.灼光 >= 3:
            print("    灼光爆发")
            damage = int(damage * 1.5)
            self.灼光 = 0
        self.灼光 += 1
        # 判定攻击
        if other.name == "丽塔":
            if random() <= 25:
                other.passiveAbility(self, 0)
                print("    丽塔闪避成功")
                return False
            else:
                other.health -= damage
        elif other.name == "幽兰黛尔" or other.name == "布洛妮娅":
            whole = other.health + other.armer
            whole -= damage
            if whole < other.health:
                other.health = whole
                other.armer = 0
            else:
                other.armer = whole - other.health
        else:
            other.health -= damage
        if other.name == "希儿":
            other.passiveAbility(self, 0)
        return True

    def print(self):
        print(self.name, end="   ")
        defense = str(self.defense) + self.丽塔_防御降低3 * "-3" + bool(self.游云_防御降低) * f"-{self.游云_防御降低}"
        print(f"{self.health} a={self.attack} d={defense} cd={self.activeTimer} 灼光={self.灼光}")