## Base
class Character():
    def __init__(self):
        self.name = '~'
        self.maxhp = 200
        self.hp = 200
        self.maxmp = 100
        self.mp = 100
        self.str = 30
        self.int = 30

    def takedmg(self,dmg):
        if dmg >= self.hp:
            self.hp = 0
            print(f"\n{self.name} fainted.")
        else:
            self.hp -= dmg
            print(f"{self.name} took {dmg} damage!")
            print(f"\n{self.name}'s current HP: {self.hp}")

    def dealdmg(self,target):
        dmg = self.str
        print(f"\n{self.name} dealt {dmg} damage!")
        target.takedmg(dmg)

## Warrior
class Warrior(Character):
    def __init__(self):
        self.name = '~'
        self.maxhp = 300
        self.hp = 300
        self.maxmp = 100
        self.mp = 100
        self.str = 50
        self.int = 10

    def special(self,target): # uppercut
        if self.mp >= 50:
            self.mp -= 50
            dmg = self.str * 2
            print(f"\n{self.name} used Uppercut.")
            print(f"{self.name} dealt {dmg} damage!")
            target.takedmg(dmg)

        else:
            dmg = self.str
            print("\nInsufficient MP!" + f" {self.name} used a normal attack.")
            print(f"{self.name} dealt {dmg} damage!")
            target.takedmg(dmg)

## Berserker
class Berserker(Character):
    def __init__(self):
        self.name = '~'
        self.maxhp = 300
        self.hp = 300
        self.maxmp = 50
        self.mp = 50
        self.str = 50
        self.int = 10

    def special(self,target): # rage
        if self.hp > self.maxhp//2:
            self.hp -= (self.maxhp//2)
            self.str += 50
            print(f"\n{self.name} used rage. {self.name} hurt himself and increased his strength!")
            print(f"{self.name}'s strength increased by 50.")

        else: print("\nYour HP is too low! Rage cannot be used.")

## Mage
class Mage(Character):
    def __init__(self):
        self.name = '~'
        self.maxhp = 200
        self.hp = 200
        self.maxmp = 200
        self.mp = 200
        self.str = 30
        self.int = 50

    def special(self,target): # fireball
        if self.mp >= 50:
            self.mp -= 50
            dmg = self.int * 2
            print(f"\n{self.name} used Fireball.")
            print(f"{self.name} dealt {dmg} damage!")
            target.takedmg(dmg)

        else:
            dmg = self.str
            print("\nInsufficient MP!" + f" {self.name} used a normal attack.")
            print(f"{self.name} dealt {dmg} damage!")
            target.takedmg(dmg)

## Weaker Enemy
class gMinion(Character):
    def __init__(self):
        super().__init__()
        self.name = "Goblin Minion"

## Stronger Enemy
class gBoss(Character):
    def __init__(self):
        super().__init__()
        self.name = "Goblin Boss"
        self.maxhp = 300
        self.hp = 300
        self.str = 50

## test
# me = Warrior()
# me.name = input("Enter your name: ")
# print(me.name)
# me.dealdmg()

# bozz = Boss()
# print(bozz.name)
# bozz.dealdmg()
