def damage_calculator(resistance, damage_dealt): 
    if resistance >= 0:
        damage_multiplier = 100/(100 + resistance)
    else: 
        damage_multiplier = 2 - (100/(100 - resistance))
    return damage_multiplier*damage_dealt

def raw_damage_calc(ratio, power):
    return ratio*power

ahri = {
    "q": {"name" : "Orb of Deception", "ratio" : 0.35}, 
    "w": {"name" : "Fox-Fire", "ratio" : 0.48}, 
    "e": {"name" : "charm", "ratio" : 0.40}, 
    "r" : {"name" : "Sprit Rush", "ratio" : 1.05}
}
print(ahri["q"]["name"])
print(damage_calculator(30, raw_damage_calc(ahri["q"]["ratio"], 100)))