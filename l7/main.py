import Game_classes as gc

army1 = gc.Army()
army2 = gc.Army()

army1.add_members(gc.Warrior, 2)
army1.add_members(gc.Fighter, 1)
army1.add_members(gc.Paladin, 1)
army1.add_members(gc.Mage, 2)

army2.add_members(gc.Paladin, 1)
army2.add_members(gc.Fighter, 1)
army2.add_members(gc.Warrior, 2)
army2.add_members(gc.Mage, 2)
army2.add_members(gc.Paladin, 1)

print(f'Army {"1" if gc.Battle.fight(army1, army2) else "2"} win')