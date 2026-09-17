from character import *

class 科拉莉(Character):
    def __init__(self):
        super().__init__()
        self.name = "科拉莉"
        self.health = 100
        self.attack = 17
        self.defense = 6
        self.speed = 21

        self.abilityCD = 3
        self.activeTimer = 3

    def activeAbility(self, other : Character, config):
        print("    科拉莉正在打哈欠")
        if self.normalAttack(other, 25):
            self.normalAttack(other, 15, True, False)
            self.normalAttack(other, 15, True, False)

    def normalAttack(self, other : Character, attack = -1, unAvoidable = False, isMain = True):
        result = super().normalAttack(other, attack)
        if result:
            if random() <= 25 and isMain:
                other.buffList.append(眩晕(other, 2))
                if other.name == "希儿":
                    other.passiveAbility(self, 1)
                print("    对方被科拉莉大人迷晕了")
