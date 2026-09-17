def random():
    from random import randint
    return randint(1, 100)

class Buff:
    owner = None
    name = "默认buff"
    timer = 1
    def __init__(self, owner:Character, timer):
        self.owner = owner
        self.timer = timer
    def run(self):
        self.timer -= 1
    def print(self):
        print(f"{self.name} {self.timer}")

class 眩晕(Buff):
    def __init__(self, owner, timer):
        super().__init__(owner, timer)
        owner.眩晕 += 1
        self.name = "眩晕"
    def run(self):
        self.timer -= 1
        if self.timer == 0 and self.owner.眩晕 > 0:
            self.owner.眩晕 -= 1

class Character:
    name = "默认角色"

    health = 100
    attack = 20
    defense = 10
    speed = 20

    buffList = []
    丽塔_防御降低3 = False
    时间禁锢 = False
    眩晕 = False
    游云_防御降低 = 0

    def __init__(self):
        pass

    # 输出表示是否命中
    def normalAttack(self, other : Character, attack = -1, unAvoidable = False):
        defense = other.defense - other.游云_防御降低
        if other.丽塔_防御降低3:
            defense -= 3
        if attack == -1:
            attack = self.attack
        if other.name == "丽塔" and not unAvoidable:
            if random() <= 25:
                other.passiveAbility(self, 0)
                print("    丽塔闪避成功")
                return False
            else:
                other.health -= max(attack - defense, 0)
        elif other.name == "幽兰黛尔" or other.name == "布洛妮娅":
            whole = other.health + other.armer
            whole -= max(attack - defense, 0)
            if whole < other.health:
                other.health = whole
                other.armer = 0
            else:
                other.armer = whole - other.health
        else:
            other.health -= max(attack - defense, 0)
        if other.name == "希儿":
            other.passiveAbility(self, 0)
        return True

    abilityCD = 2
    activeTimer = 2
    def activeAbility(self, other : Character, config):
        self.normalAttack(other, 30)

    def passiveAbility(self, other : Character, config):
        pass

    def run(self, other : Character):
        if self.眩晕:
            print(f"    {self.name}：我怎么晕乎乎的...不玩了")
            return
        self.activeTimer -= 1
        if self.activeTimer == 0:
            self.activeAbility(other, 0)
        else:
            self.normalAttack(other)

    def finish(self, other : Character):
        if self.activeTimer == 0:
            self.activeTimer = self.abilityCD

        buffCounter = 0
        while buffCounter < len(self.buffList):
            buff = self.buffList[buffCounter]
            buff.run()
            if buff.timer == 0:
                self.buffList.pop(buffCounter)
                continue
            buffCounter += 1

    def print(self):
        print(self.name, end = "   ")
        defense = str(self.defense) + self.丽塔_防御降低3 * "-3" + bool(self.游云_防御降低) * f"-{self.游云_防御降低}"
        print(f"{self.health} a={self.attack} d={defense} cd={self.activeTimer}")