import random
import Cmonster
import Citem as item
import time


def move(ich, userinput):
    if userinput == "dmg":
        if len(ich.rightHand) > 0:
            print("In deiner rechten Hand befindet sich:", ich.rightHand[0].name, ": ", ich.rightHand[0].dmg)
        if len(ich.leftHand) > 0:
            print("In deiner liken Hand befindet sich:", ich.leftHand[0].name, ": ", ich.leftHand[0].dmg)
        if len(ich.rightHand) == 0:
            print("da ist keine waffe")

    if userinput == "links":
        newPos = [ich.positionX - 1, ich.positionY]
        if not already_been_there(ich, newPos):
            face_a_monster(ich)
        ich.positionX -= 1
        ich.alreadyBeenHere.append([ich.positionX, ich.positionY])

    elif userinput == "rechts":
        newPos = [ich.positionX + 1, ich.positionY]
        if not already_been_there(ich, newPos):
            face_a_monster(ich)
        ich.positionX += 1
        ich.alreadyBeenHere.append([ich.positionX, ich.positionY])

    elif userinput == "hoch":
        newPos = [ich.positionX, ich.positionY + 1]
        if not already_been_there(ich, newPos):
            face_a_monster(ich)
        ich.positionY += 1
        ich.alreadyBeenHere.append([ich.positionX, ich.positionY])

    elif userinput == "runter":
        newPos = [ich.positionX, ich.positionY - 1]
        if not already_been_there(ich, newPos):
            face_a_monster(ich)
        ich.positionY -= 1
        ich.alreadyBeenHere.append([ich.positionX, ich.positionY])


def help():
    print("Das sind alle Befehle zum ausführen")
    print("")


def already_been_there(ich, newPos):
    if newPos in ich.alreadyBeenHere:
        print("Du warst schonmal hier")
        if ich.currentHP < ich.maxHP and ich.currentHP != (ich.maxHP - 1):
            ich.currentHP = ich.currentHP + 2
        return True


def prepare_to_fight(ich, monster):
    userInput = input("Willst du kämpfen?\n")
    if userInput == "ja":
        fight(ich, monster)
    else:
        print("heute hast du nochmal glück gehabt")


def fight(ich, monster):
    infight = True

    while infight:
        time.sleep(0.5)
        whoStarts = random.randrange(1, 10) + ich.init - monster.init
        if whoStarts >= 5:
            print("du beginnst")
            monster.currentHP = monster.currentHP - ich.dmg
            print(monster.name, " hat noch", monster.currentHP, "von ", monster.maxHP)
            ich.currentHP = ich.currentHP - (monster.dmg-(ich.armorValue/10))
            print("Du hast nur noch ", ich.currentHP, "von ", ich.maxHP)
        else:
            print("das monster beginnt")
            ich.currentHP = ich.currentHP - (monster.dmg-(ich.armorValue/10))
            print("Du hast nur noch ", ich.currentHP, "von ", ich.maxHP)
            monster.currentHP = monster.currentHP - ich.dmg
            print(monster.name, " hat noch", monster.currentHP, "von ", monster.maxHP)
        if ich.currentHP <= 0:
            print("Du bist tot")
            exit()
        elif monster.currentHP <= 0:
            print("Das monster ist tot")
            loot(ich, monster)
            print("Du überlebst den Kampf mit", monster.name, "und das mit", ich.currentHP, "HP")
            infight = False


def loot(ich, monster):
    goldDrop = random.randrange(0, 20)
    wapponDrop = random.randrange(0, 30)
    potionDrop = random.randrange(10, 30)
    if goldDrop >= 10:
        lootedValue = random.randrange(1, 3) * monster.rarity
        ich.valet = ich.vallet + lootedValue
        print("Du erhälst ", lootedValue, "Taler")
    if wapponDrop >= 10:
        possibleDrops = [item.wappon1, item.wappon2, item.wappon3, item.wappon4]
        chossenDrop = random.choice(possibleDrops)
        if len(ich.rightHand) == 0:
            ich.rightHand.append(chossenDrop)
            print("Du findest ", chossenDrop.name, )
            ich.dmg = ich.dmg + chossenDrop.dmg
            print("aktuelle rechte Hand", ich.rightHand[0].name)

        else:
            if len(ich.leftHand) == 0:
                ich.leftHand.append(chossenDrop)
                ich.dmg = ich.dmg + chossenDrop.dmg
                print("aktuelle linke Hand", ich.leftHand[0].name)
        if potionDrop >= 10:
            possibleDrops = [item.heath_pottionNR1, item.heath_pottionNR2, item.mana_potionNR1, item.mana_potionNR2]
            chossenDrop = random.choice(possibleDrops)
            ich.inventar.append(chossenDrop)
            print("du erhälst", chossenDrop.name)


def XP_calculation():
    pass


def level_up():
    pass


def rest(ich):
    print("du hattest einen schrecklichen traum, du wurdest verzaubert und hast vergessen wo du überlal schon warst")
    ich.alreadyBeenHere = [[]]
    print(ich.alreadyBeenHere)


def shopping():
    pass


def look_in_inventar():
    pass


def use_item(ich):
    ich.currentHP = ich.maxHP


def face_a_monster(ich):
    hitAMonster = random.randrange(0, 20)
    if hitAMonster < 10:
        # name, dmg, init, currentHP, maxHP, currentMP, maxMP, giveXP, rarity

        mosnter1 = Cmonster.monster("Wolf", 2, 6, 20, 20, 50, 50, 10, 1)
        monster2 = Cmonster.monster("Bär", 3, 4, 25, 25, 50, 50, 15, 1)
        mosnter3 = Cmonster.monster("Aasfresser", 2, 5, 20, 20, 50, 50, 10, 1)
        monster4 = Cmonster.monster("Rießen Ratte", 2, 7, 15, 15, 50, 50, 8, 1)
        monster5 = Cmonster.monster("Eidechse", 1, 2, 10, 10, 10, 10, 10, 1)
        monster6 = Cmonster.monster("Fuchs", 2, 3, 20, 20, 20, 20, 10, 1)
        monster7 = Cmonster.monster("Bienen Schwarm", 3, 3, 10, 10, 10, 10, 8, 1)
        monster8 = Cmonster.monster("Zecke", 1, 1, 2, 2, 0, 0, 2, 1)
        monster9 = Cmonster.monster("Warg", 5, 3, 25, 25, 10, 10, 20, 2)
        monster10 = Cmonster.monster("Bandit", 8, 3, 30, 30, 30, 30, 20, 2)

        chooseAMonster = random.choice([mosnter1, monster2, mosnter3, monster4, monster5, monster6, monster7, monster8, monster9, monster10])
        print("Du kämpfst gegen", chooseAMonster.name)
        prepare_to_fight(ich, chooseAMonster)


def calc_armor(ich):
    for armorPice in ich.armor:
        ich.armorValue = ich.armorValue + armorPice.armorValue
    return ich.armorValue
