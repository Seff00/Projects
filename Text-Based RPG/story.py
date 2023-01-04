from battle import *
from characters import *
from random import random

'''
## challenges:

1. create characters (or "classes" in RPGs) - characters.py
-1.1 default character stats
-1.2 "take damage" attribute
-1.3 "deal damage" attribute
-1.4 create enemy python class 

2. create story - story.py
-2.1 create a storyline and output with print
-2.2 create at least 3 locations (start -> middle -> end)
-2.3 allow the player to make a choice/decision at each location/stage

3. create initialise function - battle.py
-3.1 ask player to enter a name and choose a character class
-3.2 return the chosen character class

4. create battle function - battle.py
-4.1 determine who goes first 
-4.2 create list of possible inputs (see appendix A)
-4.3 ask player to enter a command/input (see battle.py file)
-4.4 enemy's turn to attack

## additional challenges to implement: 
1. locations
-1.1 increase player options at each location - use a list/dictionary (see appendix B)
-1.2 include "locations" option (text-based)
-1.3 implement a map function and remove "locations" in options (requires array knowledge)
-1.4 include deadends in the storyline/map [implemented]

2. enemies
-2.1 enemies spawn randomly instead of being predetermined (use random module) [implemented]
-2.2 different types of enemies [implemented]
-2.3 include stronger boss battles with unique abilities

3. player
-3.1 create characters with different stats [implemented]
-3.2 add a unique attack for each character type via "special" attribute  [implemented]
-3.3 critical damage: (deals more damage) for attacks at a X% chance (use random module)

## appendix:
# A - used in battle.py
battle_options = ["help","attack","special","heal","run","status"]

# B - not used
overworld_options = ["help","explore","rest","status","stats","location","quit"]
'''

print("\n>> Welcome to Venezuela, where heroes and monsters reside.")
print(">> You are a young, new adventurer ready to set foot into the unknown.\n")

p = initialise()

print("\n>> Awesome, you're all set! Let's begin your adventure!\n")
_ = input("[Press enter to continue]")

print("\n========================= (~ ^ o . o ^ )~ =========================\n")

location = "Entrance"
print(f">> {p.name} is currently at the entrance of a large cave.")
print(">> Rumour has it that a precious gemstone, The World, is inside the cave.")
print(f">> {p.name} peered into the cave but it was too dark to make out anything inside.")
    
print("\nEnter the cave? ")
p_choice = input("Enter [yes]/[no]: ")

if p_choice.lower() == "yes":
    print(f"\n>> Mustering some courage, {p.name} entered the cave to find the rumoured treasure chest.")

elif p_choice.lower() == "no":
    print(f"\n>> An unknown force pushed {p.name} in anyway...")

    print(f"\n{p.name} took 5 damage.")
    p.hp -= 5 # lmao...

else: print(f"\n[Unknown input received]\n>> An unknown force pushed {p.name} in anyway...")

print("\n========================= (~ ^ o . o ^ )~ =========================\n")

location = "Cave Level 1"
print(f">> Squinting into the darkness, {p.name} managed to make out a fork in the cave.")

print("\nChoose the right path or the left path?")
p_choice = input("Enter [right]/[left]: ")

valid = False # error checking
while not valid:
    if p_choice.lower() == "right":
        print(f"\n{p.name} chose the right path (haha geddit), and discovered a Ginseng potion.")

        print(f"\n{p.name}'s maximum hp increased by 20!")
        p.maxhp += 20

        valid = True

    elif p_choice.lower() == "left":
        print(f"\n{p.name} encountered an enemy!")
        
        battle()

        valid = True

    else:
        print('\nYou have entered an invalid choice. Please enter "right" or "left".')
        p_choice = input("Enter [right]/[left]: ")

_ = input("\n[Press enter to continue]")

print("\n========================= (~ ^ o . o ^ )~ =========================\n")

location = "Cave Level 2"
print(f">> Proceeding forward, {p.name} found another fork in the cave. However, this time it was a three-way fork.")

print("\nChoose the right, middle or left path?")
p_choice = input("Enter [right]/[middle]/[left]: ")

valid = False # error checking
while not valid:
    if p_choice.lower() == "right": # dead end
        print(f"\n>> {p.name} followed the right path, but it eventually came to a dead end.")
        print("Choose another path!")

        p_choice = input("Enter [middle]/[left]: ")

    elif p_choice.lower() == "middle": # 33.3% chance to encounter an enemy
        if random() < 0.333:
            print(f"\n{p.name} encountered an enemy!")
        
            battle()

        else:
            print(f"\n>> {p.name} passed through the tunnel, and it was eerily quiet.")
        
        valid = True

    elif p_choice.lower() == "left": # predetermined enemy
        print(f"\n{p.name} encountered an enemy!")
        
        battle()

        valid = True

    else:
        print('\nYou have entered an invalid choice. Please enter "right", "middle" or "left".')
        p_choice = input("Enter [right]/[middle]/[left]: ")

_ = input("\n[Press enter to continue]")

print("\n========================= (~ ^ o . o ^ )~ =========================\n")

location = "Treasure Room"

print(f">> {p.name} discovered the treasure room!")
print(">> Sunlight from a hole in the ceiling of the cave poured into the room, lighting up a large treasure chest in the middle of it.")
print(f">> {p.name} walked up to the treasure chest and opened it.")
print(">> A single piece of paper laid in the large chest.")

print("\nPick up the piece of paper and read it? ")
p_choice = input("Enter [yes]/[no]: ")

if p_choice.lower() == "yes":
    print("\n>> There was a link written on the piece of paper:")
    print("https://www.youtube.com/watch?v=EE-xtCF3T94")
    print("\n********** You have completed the game. Thanks for playing! **********")

elif p_choice.lower() == "no":
    print(f"\n>> {p.name} tore up the paper without reading it and went home.") 
    print("\n********** You have completed the game. Thanks for playing! **********")

else:
    print(f"\n[Unknown input received]\n>> {p.name} felt a sharp pain at the back of his head and blacked out...")
    print("\n********** You have completed the game. Thanks for playing! **********")

print(" ")
