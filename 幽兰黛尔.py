from character import *

class 幽兰黛尔(Character):
    armer = 0

    def __init__(self):
        super().__init__()
        self.name = "幽兰黛尔"
        self.health = 100
        self.attack = 16
        self.defense = 11
        self.speed = 22

        self.abilityCD = 2
        self.activeTimer = 2

    def activeAbility(self, other : Character, config):
        self.normalAttack(other, 15)
        if random() <= 20:
            print("    幽兰黛尔连击成功")
            self.normalAttack(other, 25)
        else:
            print("    幽兰黛尔连击失败")

    def normalAttack(self, other : Character, attack = -1):
        self.armer += 3
        return super().normalAttack(other, attack)

    def print(self):
        print(self.name, end="   ")
        defense = str(self.defense) + self.丽塔_防御降低3 * "-3" + bool(self.游云_防御降低) * f"-{self.游云_防御降低}"
        print(f"{self.health}+{self.armer} a={self.attack} d={defense} cd={self.activeTimer}")