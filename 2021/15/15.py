from math import inf

with open("input.txt") as f:
	texte = f.read()

# texte = """1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581"""

# poids de toutes les coordonnées
matrice = [[int(j) for j in i] for i in texte.splitlines()]

poids = dict()
for i in range(len(matrice)):
	for j in range(len(matrice[i])):
		poids[(i,j)] = matrice[i][j]

# Ensemble de toutes les coordonnées de la matrice
E = set()
for i in poids:
	E.add(i)

# renvoie l'ensemble de toutes les positions qui ne valent pas inf
def init_ensemble(d):
	return {i for i in d if d[i]!=inf}

# initialise toutes les valeurs de d à l'infini sauf le point de départ qui vaut 0 et ses voisins qui gardent leur valeur
def initialisation():
	d = {i:inf for i in poids}
	d[(0,0)] = 0
	d[(0,1)] = poids[(0,1)]
	d[(1,0)] = poids[(1,0)]
	return d

# renvoie l'ensemble de tous les voisins de p
def voisins(p):
	x,y = p
	res = set()
	if x < len(matrice)-1:
		res.add((x+1,y))
	if y < len(matrice[0])-1:
		res.add((x,y+1))
	if x > 0:
		res.add((x-1,y))
	if y > 0:
		res.add((x,y-1))
	return res

# renvoie les coordonnées qui ont le poids le plus faible
def trouve_min(E,d):
	mini = inf
	for position in E:
		if d[position]<mini:
			mini = d[position]
			p = position
	return p

# si 
def maj_distance(p1,p2,d,E):
	if d[p2] > d[p1] + poids[(p2[0],p2[1])]:	
		E.add(p2)
		d[p2] = d[p1] + poids[(p2[0],p2[1])]

# algorithme principal
def dijkstra():
	d = initialisation()
	E = init_ensemble(d)
	while E:
		p = trouve_min(E,d)
		E.discard(p)
		for voisin in voisins(p):
			maj_distance(p,voisin,d,E)
	return d[(len(matrice)-1,len(matrice[0])-1)]

print("Partie 1 :",dijkstra())

def affichage(matrice):
	for i in matrice:
		for j in i:
			print(j, end=' ')
		print()
	print()

def copie(matrice):
	return [[j for j in i] for i in matrice]

temp = copie(matrice)
for k in range(1,5):	
	for i in range(len(temp)):
		for j in range(len(temp[i])):
			matrice[i].append(((temp[i][j]+k)%10+1 if temp[i][j]+k>9 else (temp[i][j]+k)%10))
temp = copie(matrice)
for k in range(1,5):
	for i in range(len(temp)):
		matrice.append([])
		for j in range(len(temp[i])):
			matrice[-1].append(((temp[i][j]+k)%10+1 if temp[i][j]+k>9 else (temp[i][j]+k)%10))

poids = dict()
for i in range(len(matrice)):
	for j in range(len(matrice[i])):
		poids[(i,j)] = matrice[i][j]

# Ensemble de toutes les coordonnées de la matrice
E = set()
for i in poids:
	E.add(i)

# attendre environ 15 secondes pour la partie 2
print("Partie 2 :",dijkstra())