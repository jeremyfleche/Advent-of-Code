from itertools import combinations
from math import inf

weapons="""Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0
"""

armor="""Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5
"""

rings="""Damage+1    25     1       0
Damage+2    50     2       0
Damage+3   100     3       0
Defense+1   20     0       1
Defense+2   40     0       2
Defense+3   80     0       3
"""

armes=[]
ligne=[]
temp=''
for i in weapons:
	if i=='\n':
		ligne.append(temp)
		temp=''
		armes.append(ligne)
		ligne=[]
	elif i==' ':
		if temp!='':
			ligne.append(temp)
			temp=''
	else:
		temp+=i

#------------------------------------

armure=[]
ligne=[]
temp=''
for i in armor:
	if i=='\n':
		ligne.append(temp)
		temp=''
		armure.append(ligne)
		ligne=[]
	elif i==' ':
		if temp!='':
			ligne.append(temp)
			temp=''
	else:
		temp+=i
armure.append(['rien','0','0','0'])

#------------------------------------

anneaux=[]
ligne=[]
temp=''
for i in rings:
	if i=='\n':
		ligne.append(temp)
		temp=''
		anneaux.append(ligne)
		ligne=[]
	elif i==' ':
		if temp!='':
			ligne.append(temp)
			temp=''
	else:
		temp+=i
anneaux.append(['rien','0','0','0'])

#------------------------------------

print(armure)
combinaisons_armes=list(combinations(armes,1))
combinaisons_armure=list(combinations(armure,1))
combinaisons_anneaux=list(combinations(anneaux,2))+list(combinations(anneaux,1))


def victoire(arme,armure,anneaux):

	pv_boss=103
	degats_boss=9
	armure_boss=2

	pv_joueur=100
	degats_joueur=0
	armure_joueur=0
	cost=0

	for i in arme:
			cost+=int(i[1])
			degats_joueur+=int(i[2])

	for i in armure:
			cost+=int(i[1])
			armure_joueur+=int(i[3])

	for i in anneaux:
			cost+=int(i[1])
			degats_joueur+=int(i[2])
			armure_joueur+=int(i[3])

	duree_vie_boss=0
	while pv_boss>0:
		if (degats_joueur-armure_boss)<=0:
			pv_boss-=1
		else:
			pv_boss-=(degats_joueur-armure_boss)
		duree_vie_boss+=1

	duree_vie_joueur=0
	while pv_joueur>0:
		if (degats_boss-armure_joueur)<=0:
			pv_joueur-=1
		else:
			pv_joueur-=(degats_boss-armure_joueur)
		duree_vie_joueur+=1

	if duree_vie_joueur>=duree_vie_boss:
		return cost
	return inf

min_cost=inf
for arme in combinaisons_armes:
	for armure in combinaisons_armure:
		for anneaux in combinaisons_anneaux:
			if min_cost>victoire(arme,armure,anneaux):
				min_cost=victoire(arme,armure,anneaux)

print(f'Partie 1 : {min_cost}')

# Partie 2

def defaite(arme,armure,anneaux):

	pv_boss=103
	degats_boss=9
	armure_boss=2

	pv_joueur=100
	degats_joueur=0
	armure_joueur=0
	cost=0

	for i in arme:
			cost+=int(i[1])
			degats_joueur+=int(i[2])

	for i in armure:
			cost+=int(i[1])
			armure_joueur+=int(i[3])

	for i in anneaux:
			cost+=int(i[1])
			degats_joueur+=int(i[2])
			armure_joueur+=int(i[3])

	duree_vie_boss=0
	while pv_boss>0:
		if (degats_joueur-armure_boss)<=0:
			pv_boss-=1
		else:
			pv_boss-=(degats_joueur-armure_boss)
		duree_vie_boss+=1

	duree_vie_joueur=0
	while pv_joueur>0:
		if (degats_boss-armure_joueur)<=0:
			pv_joueur-=1
		else:
			pv_joueur-=(degats_boss-armure_joueur)
		duree_vie_joueur+=1

	if duree_vie_joueur<duree_vie_boss:
		return cost
	return -inf

max_cost=-inf
for arme in combinaisons_armes:
	for armure in combinaisons_armure:
		for anneaux in combinaisons_anneaux:
			if max_cost<defaite(arme,armure,anneaux):
				max_cost=defaite(arme,armure,anneaux)

print(f'Partie 2 : {max_cost}')