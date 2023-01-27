class Item:
    def __init__(self, Cost, Power, HP, MagicResist, Armor):
        self.Cost = Cost
        self.power = Power
        self.HP = HP
        self.MagicResist = MagicResist
        self.Armor = Armor
    def passive(self, champion):
        pass

class Rabadons(Item):
    def passive(self, champion):
        champion.power = champion.power * 1.4

class Protobelt(Item):
    def passive(self, champion):
        champion.power = champion.power * 1.25

# rylais = Item(2600, 90, 300, 0, 0)

# morellonomicon = Item(3000, 70, 300, -15, 0)

# rabadons_deathcap = Rabadons(3600, 120, 0, 0, 0)
