from character import *

class 琪亚娜(Character):

    def __init__(self):
        super().__init__()
        self.name = "琪亚娜"
        self.health = 100
        self.attack = 16
        self.defense = 8
        self.speed = 23

        self.abilityCD = 2
        self.activeTimer = 2

    def activeAbility(self, other : Character, config):
        if self.normalAttack(other, 20):
            other.health -= max(int(other.health * 0.15), 1)  # 向下取整，但至少为1
            if other.name == "希儿":
                other.passiveAbility(self, 0)
        self.normalAttack(other)
        print("    琪亚娜开大了！")




