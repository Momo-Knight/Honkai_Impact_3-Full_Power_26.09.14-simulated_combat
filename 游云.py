from character import *

class 游云(Character):

    double = False

    def __init__(self):
        super().__init__()
        self.name = "游云"
        self.health = 100
        self.attack = 20
        self.defense = 7
        self.speed = 25

        self.abilityCD = 3
        self.activeTimer = 3

    def run(self, other : Character):
        self.passiveAbility(other, 0)
        super().run(other)

    def activeAbility(self, other : Character, config):
        print("    绝对认真的炮击！")
        self.normalAttack(other, 22)
        self.double = True

    论文指导_防御降低 = 0
    论文指导_伤害增加 = 0
    def passiveAbility(self, other : Character, config):
        r = random()
        word = ""
        if r <= 11:
            word = "回血"
            if self.double:
                word = "超级" + word
                self.health = min(self.health + 24, 100)
                self.double = False
            else:
                self.health = min(self.health + 12, 100)
        elif r <= 22:
            word = "狂攻"
            if self.double:
                word = "超级" + word
                self.论文指导_伤害增加 = 30
                self.double = False
            else:
                self.论文指导_伤害增加 = 15
        elif r <= 33:
            word = "破防对手"
            if self.double:
                word = "超级" + word
                self.论文指导_防御降低 += 4
                self.double = False
            else:
                self.论文指导_防御降低 += 2
        if word != "":
            word = "    游云" + word
            print(word)

    def normalAttack(self, other : Character, attack = -1):
        if attack == -1:
            attack = self.attack
        super().normalAttack(other, attack + self.论文指导_伤害增加)
        self.论文指导_伤害增加 = 0

    def finish(self, other):
        other.游云_防御降低 += self.论文指导_防御降低
        self.论文指导_防御降低 = 0
        super().finish(other)

    def print(self):
        print(self.name, end="   ")
        defense = str(self.defense) + self.丽塔_防御降低3 * "-3" + bool(self.游云_防御降低) * f"-{self.游云_防御降低}"
        print(f"{self.health} a={self.attack} d={defense} cd={self.activeTimer} " + self.double * "超级加倍")