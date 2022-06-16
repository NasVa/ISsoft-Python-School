class Warrior:
    def __init__(self):
        self.health = 30
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0

    def attackEnemy(self, enemy):
        enemy.health -= self.attack

    def beAttacked(self, damage):
        self.health += - damage

    def __repr__(self):
        return f'Type : {self.__class__.__name__}, Health : {self.health}, Damage : {self.attack}'

    def __add__(self, other):
        self.health += other
        self.attack += 2

    def __mul__(self, other):
        self.health *= other
        self.attack *= 2

class Fighter(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7

class Mage(Warrior):
    def __init__(self):
        self.health = 40
        self.attack = 3
        self.magic = 6

    def attackEnemy(self, enemy):
        enemy.beAttacked(self.attack + (self.magic if enemy.attack < self.magic else 0))

    def beAttacked(self, damage):
        if damage > self.magic:
            self.health += - damage + self.magic

    def __repr__(self):
        return super().__repr__() + f', Magic : {self.magic}'

class Paladin(Warrior):
    def __init__(self):
        self.health = 50
        self.attack = 6
        self.firstAttack = 0

    def attackEnemy(self, enemy):
        if self.firstAttack:
            enemy.beAttacked(self.firstAttack / 2)
            self.firstAttack = 0
        else:
            if hasattr(enemy, 'magic'):
                enemy.beAttacked(enemy.health + enemy.magic)
                self.firstAttack = enemy.health + enemy.magic
            else:
                self.firstAttack = enemy.health
                enemy.beAttacked(enemy.health)

def fight(firstWarrior, secondWarrior):
    step = 0
    while firstWarrior.is_alive and secondWarrior.is_alive:
        if step % 2:
            secondWarrior.attackEnemy(firstWarrior)
        else:
            firstWarrior.attackEnemy(secondWarrior)
        step += 1
    return firstWarrior.is_alive


class Army:
    def __init__(self):
        self.warriors = []

    def add_members(self, type, num):
        for i in range(num):
            self.warriors.append(type())

    def __add__(self, other):
        for warrior in warriors:
            warrior.__add__(other)

    def __mul__(self, other):
        for warrior in warriors:
            warrior.__mul__(other)

class Battle:
    def fight(army1, army2):
        step = 0
        while len(army1.warriors) > 0 and len(army2.warriors) > 0:
            if step % 2:
                if army1.warriors[0].__class__== Paladin:
                    fight(army1.warriors[0], army2.warriors[0])
                    del army2.warriors[0]
                if len(army1.warriors) > 0 and len(army2.warriors) > 0:
                    isFirstArmy = not fight(army1.warriors[0], army2.warriors[0]) 
            else:
                if army2.warriors[0].__class__ == Paladin:
                    fight(army2.warriors[0], army1.warriors[0])
                    del army1.warriors[0]
                if len(army1.warriors) > 0 and len(army2.warriors) > 0:
                    isFirstArmy = fight(army2.warriors[0], army1.warriors[0])
            if len(army1.warriors) > 0 and len(army2.warriors) > 0:
                if isFirstArmy: 
                    del army1.warriors[0] 
                else:
                    del army2.warriors[0]
                step += 1 
        return len(army1.warriors) > 0
