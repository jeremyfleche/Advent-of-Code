from itertools import combinations
from collections import deque

with open("input.txt") as f:
	texte = f.read()

# texte = """28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3"""

t = sorted([int(i) for i in texte.strip().split()])
t.insert(0, 0)
t.append(max(t)+3)

res1 = 0
res3 = 0
liste = []

for i in range(len(t)-1):
	if abs(t[i]-t[i+1]) == 1:
		res1 += 1
	if abs(t[i]-t[i+1]) == 3:
		res3 += 1

print("Partie 1 :",res1*res3)

#Partie 2

def solve(t):
	n = len(t)
	combinaisons = [0] * n 		# créer une liste vide de la même longueur que la liste
	combinaisons[0] = 1 	# il n'y a qu'une manière de connecter le premier adaptateur
	for i in range(1,n):								# On parcourt toutes les valeurs de la liste
		for j in range(i):								# On parcours toutes les valeurs de la liste inférieures à la celle de la première boucle
			if t[i] - t[j] < 4:							# Si l'écart est inférieur ou égale à trois :
				combinaisons[i] += combinaisons[j]		# on ajoute le nombre de possibilité déjà calculer pour la valeur j
	return combinaisons[-1]

print("Partie 2 :",solve(t))