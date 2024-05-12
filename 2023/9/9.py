with open("input.txt") as f:
	texte = f.read()

# texte = """0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45"""

liste = [[int(i) for i in ligne.split()] for ligne in texte.splitlines()]

# Renvoie la séquence suivant représentant les écart entre les valeurs de la liste
def suivant(liste):
	res = []
	for i in range(len(liste)-1):
		res.append(liste[i+1]-liste[i])
	return res

# renvoie vrai si la liste ne contient que des 0
def finie(liste):
	for i in liste:
		if i != 0:
			return False
	return True

# Renvoie l'historique complet de la liste jusqu'à [0, ... ,0]
def historique(liste):
	res = [liste]
	while not finie(liste):
		liste = suivant(liste)
		res.append(liste)
	return res

# Renvoie la valeur droite prédite (partie 1)
def right_value(liste):
	h = historique(liste)
	x = 0
	for i in range(len(h)-2,-1,-1):
		x += h[i][-1]
	return x

# Renvoie la valeur gauche prédite (partie 2)
def left_value(liste):
	h = historique(liste)
	x = 0
	for i in range(len(h)-2,-1,-1):
		x = h[i][0] - x
	return x

print("Partie 1 :",sum([right_value(ligne) for ligne in liste]))
print("Partie 2 :",sum([left_value(ligne) for ligne in liste]))