import Cplayer
import allTheFunctions


ich = Cplayer.spieler
ich.armorValue = allTheFunctions.calc_armor(ich)

def main():
    print("Willkommen blablabla")
    print("armor wert:", ich.armorValue)
    inprogress = True
    while inprogress:
        userinput = input("Was willst du tun? \n")
        if userinput in ["links", "rechts", "hoch", "runter"]:
            allTheFunctions.move(ich, userinput)
        elif userinput == "pos":
            print("Deine Aktuelle Position lautet:",ich.positionX, ich.positionY)
        elif userinput == "all":
            print("In der folgenden Liste sind alle Koordinaten auf denen du schon warst\n")
            print(ich.alreadyBeenHere)
        elif userinput == "hp":
            print("Du hast noch", ich.currentHP)

        elif userinput == "inv":
            if len(ich.inventar) >0:
                print("Dein Inventar:")
                for i in ich.inventar:
                    print(i.name)
            else:
                print("du hast noch keine items")

        elif userinput == "use":
            allTheFunctions.use_item(ich)











main()