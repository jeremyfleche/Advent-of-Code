with open('input.txt') as f:
	texte = f.read()

# texte = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598.."""

grille = texte.splitlines()

def est_symbole(i,j):
	return not grille[i][j].isdigit() and grille[i][j] != '.'

def nombre(pj,i,j):
	if 0<=j<len(grille[i]) and grille[i][j].isdigit():
		if j < pj:
			return nombre(j,i,j-1) + grille[i][j]
		if j > pj:
			return grille[i][j] + nombre(j,i,j+1)
		if j == pj:
			return nombre(j,i,j-1) + grille[i][j] + nombre(j,i,j+1)
	return ""

def symbole_proche(i,j,cache):
	res = False
	cache.append((i,j))
	temp = []
	for a in range(-1,2):
		for b in range(-1,2):
			if 0<=i+a<len(grille) and 0<=j+b<len(grille[i]):
				if (a,b) != (0,0) and (i+a,j+b) not in cache and est_symbole(i+a,j+b):
					return (i+a,j+b)
				if (i+a,j+b) not in cache and grille[i+a][j+b].isdigit():
					res = res or symbole_proche(i+a,j+b,cache)
	return res

def nombre_chiffre(nombre):
	res = 0
	while nombre > 0:
		nombre //= 10
		res += 1
	return res

res = 0
d = dict()
for i in range(len(grille)):
	j = 0
	while j < len(grille[i]):
		if grille[i][j].isdigit():
			a = int(nombre(j,i,j))
			x = symbole_proche(i,j,[])
			if x:
				if x not in d:
					d[x] = []
				d[x].append(a)
				res += a
			j += nombre_chiffre(a)+1
		else:
			j += 1

print("Partie 1 :",res)

res = 0
for (i,j) in d:
	if grille[i][j] == '*' and len(d[(i,j)]) == 2:
		res += d[(i,j)][0]*d[(i,j)][1]

print("Partie 2 :",res)