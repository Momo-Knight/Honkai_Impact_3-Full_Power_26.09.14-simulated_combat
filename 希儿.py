from character import *

class 希儿(Character):
    花 = 0

    def __init__(self):
        super().__init__()
        self.name = "希儿"
        self.health = 100
        self.attack = 18
        self.defense = 8
        self.speed = 26

        self.abilityCD = 3
        self.activeTimer = 3

    def activeAbility(self, other : Character, config):
        print("    爱的镰刀❤")
        self.丽塔_防御降低3 = False
        self.时间禁锢 = False
        self.眩晕 = False
        self.normalAttack(other, 15)
        if self.花 < 3:
            self.花 += 1

    def normalAttack(self, other : Character, attack = -1, unAvoidable = False, isSimple = True):
        if isSimple:
            if attack == -1:
                attack = self.attack
            attack += self.花 * 6
            self.health += self.花 * 4
            self.花 = 0
        super().normalAttack(other, attack, unAvoidable)

    def passiveAbility(self, other : Character, config):
        match(config):
            # 受伤
            case 0:
                if random() <= 35:
                    if self.花 < 3:
                        self.花 += 1
            # 异常
            case 1:
                if random() <= 30:
                    if self.花 < 3:
                        self.花 += 1

    def print(self):
        print(self.name, end="   ")
        defense = str(self.defense) + self.丽塔_防御降低3 * "-3" + bool(self.游云_防御降低) * f"-{self.游云_防御降低}"
        print(f"{self.health} a={self.attack} d={defense} cd={self.activeTimer} 花={self.花}")