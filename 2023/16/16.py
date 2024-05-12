with open("input.txt") as f:
	texte = eval(f.read()).strip()

texte = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""

grille = [[j for j in i] for i in texte.splitlines()]

def affichage(grille):
	for i in grille:
		for j in i:
			print(j,end='')
		print()
	print()

def affichage_E(E):
	for i in range(len(grille)):
		for j in range(len(grille[i])):
			print('#' if (i,j) in E else '.',end='')
		print()
	print()

def valide(i,j):
	return 0<=i<len(grille) and 0<=j<len(grille[i])

def propagation(i,j,vi,vj):
	E = set()
	SEEN = set()
	faisseau = {(i,j,vi,vj)}
	while faisseau:
		(i,j,vi,vj) = faisseau.pop()
		if (i,j,vi,vj) in SEEN or not valide(i,j):
			continue
		SEEN.add((i,j,vi,vj))
		E.add((i,j))
		if grille[i][j] == '.':
			faisseau.add((i+vi,j+vj,vi,vj))
		if grille[i][j] == '/':
			if vi == -1:
				faisseau.add((i,j+1,0,1))
			elif vi == 1:
				faisseau.add((i,j-1,0,-1))
			elif vj == -1:
				faisseau.add((i+1,j,1,0))
			else:
				faisseau.add((i-1,j,-1,0))
		if grille[i][j] == '\\':
			if vi == -1:
				faisseau.add((i,j-1,0,-1))
			elif vi == 1:
				faisseau.add((i,j+1,0,1))
			elif vj == -1:
				faisseau.add((i-1,j,-1,0))
			else:
				faisseau.add((i+1,j,1,0))
		if grille[i][j] == '|':
			if vi != 0:
				faisseau.add((i+vi,j,vi,0))
			else:
				faisseau.add((i-1,j,-1,0))
				faisseau.add((i+1,j,1,0))
		if grille[i][j] == '-':
			if vj != 0:
				faisseau.add((i,j+vj,0,vj))
			else:
				faisseau.add((i,j-1,0,-1))
				faisseau.add((i,j+1,0,1))
	return len(E)

print(propagation(0,0,0,1))

cache = dict()
def propagation2(i,j,vi,vj):
	E = set()
	SEEN = set()
	faisseau = {(i,j,vi,vj)}
	while faisseau:
		(i,j,vi,vj) = faisseau.pop()
		if (i,j,vi,vj) in SEEN or not valide(i,j):
			continue
		SEEN.add((i,j,vi,vj))
		E.add((i,j))
		if grille[i][j] == '.':
			faisseau.add((i+vi,j+vj,vi,vj))
		if grille[i][j] == '/':
			if vi == -1:
				faisseau.add((i,j+1,0,1))
			elif vi == 1:
				faisseau.add((i,j-1,0,-1))
			elif vj == -1:
				faisseau.add((i+1,j,1,0))
			else:
				faisseau.add((i-1,j,-1,0))
		if grille[i][j] == '\\':
			if vi == -1:
				faisseau.add((i,j-1,0,-1))
			elif vi == 1:
				faisseau.add((i,j+1,0,1))
			elif vj == -1:
				faisseau.add((i-1,j,-1,0))
			else:
				faisseau.add((i+1,j,1,0))
		if grille[i][j] == '|':
			if vi != 0:
				faisseau.add((i+vi,j,vi,0))
			else:
				faisseau.add((i-1,j,-1,0))
				faisseau.add((i+1,j,1,0))
		if grille[i][j] == '-':
			if vj != 0:
				faisseau.add((i,j+vj,0,vj))
			else:
				faisseau.add((i,j-1,0,-1))
				faisseau.add((i,j+1,0,1))
	return len(E)

res = 0
for i in range(len(grille)):
	# print(i*100/len(grille))
	for j in range(len(grille[i])):
		for vi,vj in [(0,1),(0,-1),(1,0),(-1,0)]:
			x = propagation2(i,j,vi,vj)
			res = x if x > res else res

print(res)