from collections import deque

with open("input.txt") as f:
	texte = f.read()

# texte = """..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ..."""

grille = [[i for i in ligne] for ligne in texte.strip().splitlines()]

def affichage(grille):
	for i in range(len(grille)):
		for j in range(len(grille[i])):
			print(grille[i][j],end="")
		print()
	print()

def start():
	for i in range(len(grille)):
		for j in range(len(grille[i])):
			if grille[i][j] == 'S':
				return i,j

def forme(x,y):
	return grille[x][y]

x,y = start()
SEEN = {(x,y)}
Q = deque([(x,y)])
possible_s = {"|", "-", "L", "J", "F", "7"}

while Q:
	x,y = Q.popleft()
	if x > 0 and forme(x,y) in "S|LJ" and forme(x-1,y) in "|F7" and (x-1,y) not in SEEN:
		Q.append((x-1,y))
		SEEN.add((x-1,y))
		if forme(x,y)=="S":
			possible_s &= {"|","J","L"}
	if x < len(grille)-1 and forme(x,y) in "S|F7" and forme(x+1,y) in "|JL" and (x+1,y) not in SEEN:
		Q.append((x+1,y))
		SEEN.add((x+1,y))
		if forme(x,y)=="S":
			possible_s &= {"|","F","7"}
	if y > 0 and forme(x,y) in "S-J7" and forme(x,y-1) in "-FL" and (x,y-1) not in SEEN:
		Q.append((x,y-1))
		SEEN.add((x,y-1))
		if forme(x,y)=="S":
			possible_s &= {"-","J","7"}
	if y < len(grille[x]) - 1 and forme(x,y) in "S-FL" and forme(x,y+1) in "-J7" and (x,y+1) not in SEEN:
		Q.append((x,y+1))
		SEEN.add((x,y+1))
		if forme(x,y)=="S":
			possible_s &= {"-","F","L"}

print("Partie 1 :",len(SEEN)//2)

for i in range(len(grille)):
	for j in range(len(grille[i])):
		if (i,j) not in SEEN:
			grille[i][j] = "."
		if grille[i][j] == 'S':
			grille[i][j] = possible_s.pop()

outside = set()																# Ensembre des coordonnées des éléments en dehors de la boucle
for i in range(len(grille)):
	dedans = False
	au_dessus = None
	for j in range(len(grille[i])):
		if forme(i,j) == "|":												# Si on franchit ce caratère, on passe de dedans à dehors ou l'inverse
			dedans = not dedans
		elif forme(i,j) in "LF":											# Si on rencontre un angle côté exterieur face à nous -> au_dessus = True si F
			au_dessus = forme(i,j) == "F"									#													  -> au dessus = False si L
		elif forme(i,j) in "J7":											# Si on rencontre un angle côté interieur face à nous
			if forme(i,j) == ("J" if au_dessus else "7"):					#	-> Si on a rencontré l'angle opposé c'est qu'on traverse
				dedans = not dedans
		if not dedans:
			outside.add((i,j))

print("Partie 2 :",len(grille)*len(grille[0]) - len(SEEN | outside))
affichage(grille)