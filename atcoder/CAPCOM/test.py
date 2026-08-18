class Buff():
    def __init__(self, turn, point):
        self.turn = turn
        self.point = point
class Hunter():
    def __init__(self, HP):
        self.name = "Hunter"
        self.HitPoint = HP
        self.MaxHitPoint = HP
        self.AttackDamage = 40
        self.PotionPoint = 80
        self.isGuard = False
        self.buffs = []

    def Attack(self, monster):
        damage = self.AttackDamage
        for buff in self.buffs:
            damage += buff.point

        monster.Attacked(damage)

    def Buff(self, x, y):
        self.buffs.append(Buff(x, y))

    def RemoveStrongestBuff(self):
        if len(self.buffs) == 0:
            return

        max_index = 0
        for i in range(len(self.buffs)):
            if self.buffs[i].point > self.buffs[max_index].point:
                max_index = i

        self.buffs.pop(max_index)
    def Potion(self):
        self.HitPoint += self.PotionPoint
        if self.HitPoint > self.MaxHitPoint: 
            self.HitPoint = self.MaxHitPoint

    def Attacked(self, point):
        if self.isGuard:
            self.isGuard = False
            return
        self.HitPoint -= point
        if self.HitPoint < 0:
            self.HitPoint = 0

    def Guard(self):
        self.isGuard  = not self.isGuard

    def DecreaseBuffTurn(self):
        for buff in self.buffs:
            buff.turn -= 1
        
        self.buffs = [buff for buff in self.buffs if buff.turn > 0]


class Monster():
    def __init__(self, HP):
        self.name = "Monster"
        self.HitPoint = HP
        self.AttackDamage = 40
        self.AngerAttackDamage = 80
        self.isAnger = 0

    def Attack(self, hunter):
        if self.isAnger:
            hunter.Attacked(self.AngerAttackDamage)
            if self.isAnger > 0: 
                self.isAnger -= 1
        else:
            hunter.Attacked(self.AttackDamage)

    def Attacked(self, point):
        self.HitPoint -= point
        if self.HitPoint < 0:
            self.HitPoint = 0

    def Anger(self):
        self.isAnger = 3

def WinnerConfirm(hunter, monster):
    if hunter.HitPoint <= 0:
        return False, monster
    elif monster.HitPoint <= 0:
        return False, hunter
    return True, None
# 入力
playerHP = int(input())
enemyHP = int(input())
actionNum = int(input())
Actions = [input().split(' ') for i in range(actionNum)]

hunter = Hunter(playerHP)
monster = Monster(enemyHP)
isGame = True
Winner = None


for id, action in enumerate(Actions):
    if id % 2 == 0:
        if action[0] == "Attack":
            hunter.Attack(monster)
            hunter.DecreaseBuffTurn()
        elif action[0] == "Potion":
            hunter.Potion()
            hunter.DecreaseBuffTurn()
        elif action[0] == "Guard":
            hunter.Guard()
            hunter.DecreaseBuffTurn()
        elif action[0] == "Buff":
            x = int(action[1])
            y = int(action[2])
            hunter.Buff(x, y)


    else:
        if action[0] == "Attack":
            monster.Attack(hunter)
        elif action[0]  == "Anger":
            monster.Anger()
        elif action[0] == "Breath":
            hunter.RemoveStrongestBuff()


    isGame, Winner = WinnerConfirm(hunter, monster)

    if not isGame:
        break

if isGame:
    Winner = monster

print(Winner.name + ' ' + str(Winner.HitPoint))

