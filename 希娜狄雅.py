from character import *

class 希娜狄雅(Character):
    def __init__(self):
        super().__init__()
        self.name = "希娜狄雅"
        self.health = 100
        self.attack = 17
        self.defense = 7
        self.speed = 25

        self.abilityCD = 3
        self.activeTimer = 3

    def activeAbility(self, other : Character, config):
        super().normalAttack(other)
        super().normalAttack(other)
        super().normalAttack(other)

    def normalAttack(self, other : Character, attack = -1, unAvoidable = False):
        if random() <= 20:
            if attack == -1:
                attack = self.attack
            attack += 10
            super().normalAttack(other, 10, unAvoidable)
            if not self.时间禁锢:
                self.attack += 1