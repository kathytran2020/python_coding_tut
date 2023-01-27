import LeagueChampions
import LeagueItems

ahri = LeagueChampions.Ahri(30, 20.8, 526, .35, .48, .40, 1.05)
rabadons_deathcap = LeagueItems.Rabadons(3600, 120, 0, 0, 0)

ahri.add_items([rabadons_deathcap])
print(ahri.full_combo_damage())