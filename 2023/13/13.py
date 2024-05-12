with open("input.txt") as f:
	texte = f.read().strip()

# texte = """#.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.

# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#"""

t = [[[i for i in ligne] for ligne in paquet.splitlines()] for paquet in texte.split("\n\n")]

def affichage(grille):
	for i in grille:
		for j in i:
			print(j, end="")
		print()
	print()

def colonne(grille, j):
	return [grille[i][j] for i in range(len(grille))]

def ligne(grille, i):
	return grille[i]

def est_symetrique(grille, mode_ligne):
	if mode_ligne:
		for i in range(len(grille)//2):
			if grille[i] != grille[len(grille)-i-1]:
				return False
		return True
	else:
		for j in range(len(grille[0])//2):
			if colonne(grille,j) != colonne(grille,len(grille[0])-j-1):
				return False
		return True

def symetrie(grille):
	for i in range(len(grille)-1):
		longueur = min(i+1, len(grille)-i-1)
		temp = grille[i-longueur+1:i+longueur+1]
		if est_symetrique(temp, True):
			return 100*(i+1)

	for j in range(len(grille[0])-1):
		longueur = min(j+1, len(grille[0])-j-1)
		temp = [ligne[j-longueur+1:j+longueur+1] for ligne in grille]
		if est_symetrique(temp, False):
			return j+1

def modification(grille, i, j):
	res = [[j for j in i] for i in grille]
	res[i][j] = '#' if res[i][j] == "." else "."
	return res

def symetrie2(grille):
	for i in range(len(grille)-1):
		longueur = min(i+1, len(grille)-i-1)
		t = grille[i-longueur+1:i+longueur+1]
		for a in range(len(t)):
			for b in range(len(t[a])):
				temp = modification(t, a, b)
				if est_symetrique(temp, True):
					return 100*(i+1)

	for j in range(len(grille[0])-1):
		longueur = min(j+1, len(grille[0])-j-1)
		t = [ligne[j-longueur+1:j+longueur+1] for ligne in grille]
		for a in range(len(t)):
			for b in range(len(t[a])):
				temp = modification(t, a, b)
				if est_symetrique(temp, False):
					return j+1

res1 = 0
res2 = 0
for i in t:
	res1 += symetrie(i)
	res2 += symetrie2(i)

print("Partie 1 :",res1)
print("Partie 2 :",res2)