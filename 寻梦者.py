from character import *

class 时间禁锢(Buff):
    def __init__(self, owner, timer):
        super().__init__(owner, timer)
        self.name = "时间禁锢"
        owner.时间禁锢 = True

    def run(self):
        self.timer -= 1
        if self.timer == 0 and self.owner.时间禁锢 == True:
            self.owner.时间禁锢 = False
            print(f"    {self.owner.name}的诅咒解除了")

class 寻梦者(Character):
    def __init__(self):
        super().__init__()
        self.name = "寻梦者"
        self.health = 100
        self.attack = 18
        self.defense = 9
        self.speed = 23

        self.abilityCD = 3
        self.activeTimer = 3

    def activeAbility(self, other : Character, config):
        print("    寻梦者释放大招")
        self.normalAttack(other, 24)
        if random() <= 20:
            other.buffList.append(时间禁锢(other, 2))
            if other.name == "希儿":
                other.passiveAbility(self, 1)
            print("    寻梦者施加时间禁锢")

    healthRecorder = [0, 0, 0, 100]
    def passiveAbility(self, other : Character, config):
        if (self.healthRecorder[0] != 0):
            self.health = self.healthRecorder[0]
            self.defense = max(self.defense - 4, 0)
            print(f"    寻梦者恢复生命值至{self.health}")

    def run(self, other : Character):
        tmp = self.healthRecorder[1:4]
        self.healthRecorder[0:3] = tmp
        self.healthRecorder[3] = self.health
        if self.health < 25 and not self.眩晕:
            self.passiveAbility(other, 0)

        super().run(other)


