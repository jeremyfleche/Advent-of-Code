with open("input.txt") as f:
	texte = f.read()

# texte = """...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#....."""

grille = [[i for i in ligne] for ligne in texte.strip().splitlines()]

def affichage():
	for i in grille:
		for j in i:
			print(j,end="")
		print()
	print()

def ligne_vide(i):
	for i in grille[i]:
		if i == "#":
			return False
	return True

def colonne_vide(j):
	for i in range(len(grille)):
		if grille[i][j] == "#":
			return False
	return True

# Renvoie l'ensemble des indice des lignes vides et celui des colonnes vides
def expansion():
	ligne = set()
	for i in range(len(grille)):
		if ligne_vide(i):
			ligne.add(i)
	colonne = set()
	for j in range(len(grille[0])):
		if colonne_vide(j):
			colonne.add(j)
	return ligne,colonne

# Renvoie la distance entre deux galaxies en prenant en compte que les lignes et colonnes vides prennent n pas à traverser à traverser
def manhattan(a,b,n,empty_line, empty_colonne):
	res = 0
	xa,ya = a
	xb,yb = b
	for ligne in empty_line:
		if xa < ligne < xb or xb < ligne < xa:
			res += n-1
	for colonne in empty_colonne:
		if ya < colonne < yb or yb < colonne <  ya:
			res += n-1
	return res + abs(xb-xa) + abs(yb-ya)

galaxies = []
for i in range(len(grille)):
	for j in range(len(grille[i])):
		if grille[i][j] == "#":
			galaxies.append((i,j))

empty_line,empty_colonne = expansion()
SEEN = set()
res1 = 0
res2 = 0
for a in galaxies:
	for b in galaxies:
		if (b,a) not in SEEN:
			res1 += manhattan(a,b,2,empty_line,empty_colonne)
			res2 += manhattan(a,b,1000000,empty_line,empty_colonne)	
			SEEN.add((a,b))
			
print("Partie 1 :",res1)
print("Partie 2 :",res2)