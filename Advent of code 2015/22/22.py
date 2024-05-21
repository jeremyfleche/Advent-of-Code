from itertools import combinations,permutations
from math import inf

def sorts(sort):

	global pv_boss
	global degats_boss
	global pv_joueur
	global mana
	global bouclier_bonus
	global degats_bonus

	if sort=='magic_missile':
		mana-=53
		pv_boss-=4
	if sort=='drain':
		mana-=73
		pv_boss-=2
		pv_joueur+=2
	if sort=='shield':
		mana-=113
		bouclier_bonus=(6,7)
	if sort=='poison':
		mana-=173
		degats_bonus=(6,3)
	if sort=='recharge':
		mana-=229
		mana_bonus=(5,101)

pv_boss=51
degats_boss=9
degats_bonus=(0,0)

pv_joueur=50
mana=500
bouclier_bonus=(0,0)
mana_bonus=(0,0)
nombre_de_tour_max=pv_joueur//(degats_boss-7)
print(nombre_de_tour_max)

sorts=['magic_missile','drain','shield','poison','recharge']

def tour():
	global sort
	global pv_boss
	global degats_boss
	global pv_joueur
	global mana
	global bouclier_bonus
	global degats_bonus
	
