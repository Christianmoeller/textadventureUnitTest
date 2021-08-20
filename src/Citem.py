#!/usr/bin/python
#coding=utf-8

class items:
    def __init__(self, name, price, rarity):
        self.name = name
        self.price = price
        self.rarity = rarity

class armor(items):
    def __init__(self, name, price, rarity, armorValue):
        super().__init__(name, price, rarity)
        self.armorValue = armorValue


class wappon(items):
    def __init__(self, name, price, rarity, dmg):
        super().__init__(name, price, rarity)
        self.dmg = dmg


class potion(items):
    def __init__(self, name, price, rarity, amount):
        super().__init__(name, price, rarity)
        self.amount = amount


# Schwerter Stufe 1
wappon1 = wappon("ein altes Schwert", 10, 1, 2)
wappon2 = wappon("ein rostiges Schwert", 12, 1, 4)

# Äxte Stufe 1
wappon3 = wappon("eine vermoderte Axt", 10, 1, 3)
wappon4 = wappon("eine alte Axt", 12, 1, 5)

# Heiltänke Stufe 1
heath_pottionNR1 = potion("kleiner Heiltrank", 5, 1, 5)
heath_pottionNR2 = potion("mittlerer Heiltrank", 8, 1, 10)

#Manatränke Stufe 1
mana_potionNR1 = potion("kleiner Manatrank", 5, 1, 5)
mana_potionNR2 = potion("mittlerer Manatrank", 8, 1, 10)

#Lederrüstung Stufe 1

leather_helmet = armor("Lederhelm", 5, 1, 5)
leather_chest = armor("Lederbrustpanzer", 5, 1, 6)
leather_gauntlet = armor("Lederhandschuhe", 5, 1, 3)
leather_laggins = armor("Lederhose", 5, 1, 5)
leather_boots = armor("Lederschuhe", 5, 1, 3)
