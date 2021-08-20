import Citem
class player:


    def __init__(self, level, dmg, init, vallet,  currentHP, maxHP, currentMP, maxMP, currentXP, maxXP, rightHand, leftHand, armor, armorValue, inventar,
                 positionX=0, positionY=0):
        self.level = level
        self.dmg = dmg
        self.init = init
        self.vallet = vallet
        self.currentHP = currentHP
        self.maxHP = maxHP
        self.currentMP = currentMP
        self.maxMp = maxMP
        self.currentEP = currentXP
        self.maxEP = maxXP
        self.rightHand = rightHand
        self.leftHand = leftHand
        self.armor = armor #liste an rüstungen
        self.armorValue = armorValue # wert der rüstung
        self.inventar = inventar
        self.positionX = positionX
        self.positionY = positionY
        self.alreadyBeenHere = [[0, 0]]


spieler = player(1, 2, 5, 0, 30, 30, 60, 60, 0, 100, [], [], [Citem.leather_helmet, Citem.leather_chest,
                                                              Citem.leather_gauntlet, Citem.leather_laggins,
                                                              Citem.leather_boots], 0, [])
