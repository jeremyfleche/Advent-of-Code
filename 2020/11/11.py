with open("input.txt") as f:
	texte = f.read()

# texte = """L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL"""

grille = [[j for j in i] for i in texte.strip().split("\n")]

def affichage(grille):
	for i in grille:
		for j in i:
			print(j, end="")
		print()

def nb_voisins(grille,i,j):
	res = 0
	for y in range(-1,2):
		for x in range(-1,2):
			try:
				if grille[i+y][j+x] == "#" and (y,x) != (0,0) and i+y >= 0 and j+x >= 0:
					res += 1
			except:
				pass
	return res

def copie(grille):
	return [[j for j in i] for i in grille]

def suivant(grille):
	res = copie(grille)
	for i in range(len(grille)):
		for j in range(len(grille[i])):
			if grille[i][j] == "L" and nb_voisins(grille,i,j) == 0:
				res[i][j] = "#"
			if grille[i][j] == "#" and nb_voisins(grille,i,j) >= 4:
				res[i][j] = "L"
	return res

def siege_occupes(grille):
	res = 0
	for i in grille:
		for j in i:
			if j == "#":
				res += 1
	return res

while grille != suivant(grille):
	grille = suivant(grille)

print("Partie 1 :",siege_occupes(grille))

#Partie 2

with open("input.txt") as f:
	texte = f.read()

# texte = """L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL"""

grille = [[j for j in i] for i in texte.strip().split("\n")]

def nombre_range(grille,i,j):
	max_i = max(len(grille)-i+1,i+1)
	max_j = max(len(grille[i])-j+1,j+1)
	return max(max_i,max_j)

def nb_voisins2(grille,i,j):
	voisins = {"N":0, "NE":0, "E":0, "SE":0, "S":0, "SO":0, "O":0, "NO":0}
	for x in range(1,nombre_range(grille,i,j)):
		if 0 not in voisins.values():
			break
		try:	
			if grille[i-x][j] != "." and voisins["N"] == 0 and i-x >= 0:
				voisins["N"] = grille[i-x][j]
		except:
			pass
		try:
			if grille[i+x][j] != "." and voisins["S"] == 0:
				voisins["S"] = grille[i+x][j]
		except:
			pass
		try:
			if grille[i][j-x] != "." and voisins["O"] == 0 and j-x >= 0:
				voisins["O"] = grille[i][j-x]
		except:
			pass
		try:
			if grille[i][j+x] != "." and voisins["E"] == 0:
				voisins["E"] = grille[i][j+x]
		except:
			pass
		try:
			if grille[i-x][j-x] != "." and voisins["NO"] == 0 and i-x >= 0 and j-x >= 0:
				voisins["NO"] = grille[i-x][j-x]
		except:
			pass
		try:
			if grille[i-x][j+x] != "." and voisins["NE"] == 0 and i-x >= 0:
				voisins["NE"] = grille[i-x][j+x]
		except:
			pass
		try:
			if grille[i+x][j-x] != "." and voisins["SO"] == 0 and j-x >= 0:
				voisins["SO"] = grille[i+x][j-x]
		except:
			pass
		try:
			if grille[i+x][j+x] != "." and voisins["SE"] == 0:
				voisins["SE"] = grille[i+x][j+x]
		except:
			pass

	res = 0
	for i in voisins:
		if voisins[i] == "#":
			res += 1
	return res

def suivant2(grille):
	res = copie(grille)
	for i in range(len(grille)):
		for j in range(len(grille[i])):
			if grille[i][j] == "L" and nb_voisins2(grille,i,j) == 0:
				res[i][j] = "#"
			if grille[i][j] == "#" and nb_voisins2(grille,i,j) >= 5:
				res[i][j] = "L"
	return res

compteur = 0
while grille != suivant2(grille):
	grille = suivant2(grille)
	compteur += 1
	print(compteur)

print("Partie 2 :",siege_occupes(grille)) # attendre environ 70 secondes pour le résultat

