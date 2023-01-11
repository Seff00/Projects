from characters import *
import random as r

## test
# p = Warrior()
# p.name = "player 1"
## test

battle_options = ["help","attack","special","heal","run","status"]

enemies = ["Goblin Minion","Goblin Boss"]

def initialise():

    global p

    p_name = input("Enter your character's name: ")

    valid = False # error checking
    while not valid:
        print("\n--------------- Available classes ---------------\n")
        print("1. Warrior: Excels in strength\n(Special skill: Uppercut)\n")
        print("2. Berserker: Excels in strength\n(Special skill: Rage)\n")
        print("3. Mage: Excels in intelligence\n(Special skill: Fireball)\n")

        p_class = input("Choose the class you would like to play: ")

        if p_class.lower() == "warrior":
            p = Warrior()

        elif p_class.lower() == "berserker":
            p = Berserker()

        elif p_class.lower() == "mage":
            p = Mage()

        else:
            print("\nYou have entered an invalid class. Please try again.")
            continue

        p.name = p_name
        valid = True

    return p

def battle():
    print("\n########## F I G H T ########## S T A R T ##########")

    # determines which enemy is encountered
    encountered = r.choice(enemies)
    print(f"\nA {encountered} is blocking {p.name}'s path!")

    if encountered == "Goblin Minion":
        e = gMinion()

    elif encountered == "Goblin Boss":
        e = gBoss()

    # determines who goes first
    turn = r.choice(["player","enemy"])

    if turn == "player":
        print(f"{p.name} was faster, and striked first.")
        print("==================================================")

    elif turn == "enemy":
        print(f"\n{e.name} was faster, and striked first.")
        print("==================================================")

    alive = True
    while alive:
        
        # checks turn
        if turn == "player":
            
            print(f'What would {p.name} do? (Enter "help" for a list of commands.)')
            action = input("Enter a command: ")

            # displays list of battle_options that player can input
            # battle_options = ["help","attack","special","heal","run","status"]
            if action.lower() == "help":
                print("")
                print(battle_options)
                print("==================================================")
                continue
            
            # basic attack (dealdmg)
            elif action.lower() == "attack":
                p.dealdmg(e)
                print("==================================================")

                turn = "enemy"

            # special attack (special)
            elif action.lower() == "special":
                p.special(e)
                print("==================================================")

                turn = "enemy"

            # heal 
            elif action.lower() == "heal":

                # checks if player is out of mana to heal
                if p.mp < 10:
                    print("Insufficient MP." + f"p.name was unable to heal.")
                    print("Please choose another command.")
                    continue

                # checks if player is hurt (0 > HP > MAXHP - 50 > MAXHP)
                if (p.maxhp-p.hp) > 50:
                    p.hp += 50
                    p.mp -= 10

                    print(f"\n{p.name} recovered 50 HP.")
                    print("==================================================")

                # checks if player's HP is full (HP = MAXHP)
                elif p.hp == p.maxhp:
                    print(f"{p.name}'s HP is full! Please choose another command.")
                    continue

                # heal to full HP
                else:
                    p.hp = p.maxhp
                    p.mp -= 10
                    print(f"\n{p.name} healed to full HP.")
                    print("==================================================")

                turn = "enemy"
            
            # flee
            elif action.lower() == "run":

                if r.random() <= 0.1: # 10% chance to flee
                    print(f"\n{p.name} fled the battle.")
                    break

                else:
                    print(f"\n{p.name} was unable to flee.")
                    print("==================================================")
                    turn = "enemy"

            # display player's current health
            elif action.lower() == "status":
                print(f"\n{p.name}'s current HP: {p.hp}/{p.maxhp}")
                print(f"{p.name}'s current MP: {p.mp}/{p.maxmp}")
                print("==================================================")
                continue
            
            # checks if input given is not in battle_options
            else:
                print("\nInvalid command. Please try again.")
                print("==================================================")
                continue
            
            # checks if enemy is dead
            if e.hp <= 0:
                alive = False

        # checks turn
        elif turn == "enemy":
            e.dealdmg(p)
            print("==================================================")

            turn = "player"
            
            # checks if player is dead
            if p.hp <= 0:
                alive = False

    print("\n########## F I G H T ########## O V E R ##########")
    
    if p.hp <= 0:
        print(f"\n>> {p.name} fainted during the battle and was never seen again...")
        print("\n********** Game over. Try again? **********")
        quit()
    
    # recovers hp and mp after each battle
    p.hp = p.maxhp
    p.mp = p.maxmp

## test
# p = initialise()
# battle()
