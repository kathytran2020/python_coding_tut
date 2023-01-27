class Champion:
    def __init__(self, MagicResist, Armor, HP, Q, W, E, R):
        self.MagicResist = MagicResist
        self.Armor = Armor
        self.HP = HP
        self.Q = Q
        self.W = W
        self.E = E
        self.R = R
        self.power = 0

    def add_items(self, items:list):
        for item in items:
            self.power += item.power 
        
        for item in items:
            item.passive(self)

    def full_combo_damage(self):
        return self.power*(self.Q + self.W + self.E + self.R)

# x = Champion(32, 33, 100, 100, 20, 30, 10)
# print(x.MagicResist)
# print(x.full_combo_damage())

class Ahri(Champion):
    def full_combo_damage(self):
        return self.power*(self.E + (self.Q + self.W + self.R)*1.2)

# ahri = Ahri(30, 20.8, 526, .35, .48, .40, 1.05)
# ahri.add_items([rabadons_deathcap, rylais])
# print(ahri.full_combo_damage())
# print(ahri.power)

def simulate_fight(x: Champion, y: Champion):
    '''How much damage two champions do to each other, calculated using full_combo_damage'''
    return x.full_combo_damage()