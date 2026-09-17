from character import *

class 防御降低3(Buff):
    def __init__(self, owner, timer):
        super().__init__(owner, timer)
        owner.丽塔_防御降低3 = True
        self.name = "丽塔_防御降低3"

    def run(self):
        self.timer -= 1
        if self.timer == 0:
            self.owner.丽塔_防御降低3 = False

class 丽塔(Character):
    def __init__(self):
        super().__init__()
        self.name = "丽塔"
        self.health = 100
        self.attack = 18
        self.defense = 8
        self.speed = 21

        self.abilityCD = 2
        self.activeTimer = 2

    def activeAbility(self, other : Character, config):
        self.normalAttack(other, 18)
        other.buffList.append(防御降低3(other, 2))
        if other.name == "希儿":
            other.passiveAbility(self, 1)
        print("    对方被丽塔破防了！")

    def passiveAbility(self, other : Character, config):
        if self.眩晕:
            return
        self.normalAttack(other, 20)