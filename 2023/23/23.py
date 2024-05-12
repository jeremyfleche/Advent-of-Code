with open("input.txt") as f:
	texte = f.read()

# texte = """#.#####################
# #.......#########...###
# #######.#########.#.###
# ###.....#.>.>.###.#.###
# ###v#####.#v#.###.#.###
# ###.>...#.#.#.....#...#
# ###v###.#.#.#########.#
# ###...#.#.#.......#...#
# #####.#.#.#######.#.###
# #.....#.#.#.......#...#
# #.#####.#.#.#########v#
# #.#...#...#...###...>.#
# #.#.#v#######v###.###v#
# #...#.>.#...>.>.#.###.#
# #####v#.#.###v#.#.###.#
# #.....#...#...#.#.#...#
# #.#########.###.#.#.###
# #...###...#...#...#.###
# ###.###.#.###v#####v###
# #...#...#.#.>.>.#.>.###
# #.###.###.#.###.#.#v###
# #.....###...###...#...#
# #####################.#"""

grille = [[j for j in i] for i in texte.strip().splitlines()]

def voisins(i,j):
	res = []
	for a,b in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
		if 0<=a<len(grille) and 0<=b<len(grille[0]) and grille[a][b] != '#':
			res.append((a,b))
	return res

# Le but est de réduire le graphe en le représentant que selon les noeuds (les points où au moins trois chemins se rejoignent)

# On génère l'ensemble des noeuds
start = (0,grille[0].index('.'))
end = (len(grille)-1,grille[-1].index('.'))
noeuds = {start, end}
for i in range(len(grille)):
	for j in range(len(grille)):
		if grille[i][j] != '#' and len(voisins(i,j)) > 2:
			noeuds.add((i,j))

# renvoie les suivants en fonctions du type de point
def directions(y,x):
	if grille[y][x] == '>': 
		return [(y,x+1)]
	if grille[y][x] == '<':
		return [(y,x-1)]
	if grille[y][x] == 'v':
		return [(y+1,x)]
	if grille[y][x] == '^':
		return [(y-1,x)]
	if grille[y][x] == '.':
		return [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]

# renvoie le graphe en fonction de la partie du porblème qu'on veut résoudre
# partie 1 : le graphe est orienté (si on marche sur pente on doit aller dans sa direction)
# partie 2 : le graphe n'est plus orienté car on n'est plus obligé de suivre la pente qu'en on est dessus
def graphe(part):
	res = {i:dict() for i in noeuds}
	for (y,x) in noeuds:
		Q = [(y,x,0,{(y,x)})]
		while Q:
			i,j,longueur,seen = Q.pop()

			if (i,j) in noeuds-{(y,x)}:
				res[(y,x)][(i,j)] = longueur
				continue

			if part == 1:
				for (a,b) in directions(i,j):
					if 0<=a<len(grille) and 0<=b<len(grille[0]) and grille[a][b] != '#' and (a,b) not in seen:
						Q.append((a,b,longueur+1,seen|{(a,b)}))
			else:
				for (a,b) in voisins(i,j):
					if 0<=a<len(grille) and 0<=b<len(grille[0]) and grille[a][b] != '#' and (a,b) not in seen:
						Q.append((a,b,longueur+1,seen|{(a,b)}))
	return res

def solve(part):
	g = graphe(part)
	res = 0
	Q = [(0,1,0,{start})]
	while Q:
		i,j,longueur,cache = Q.pop()

		if (i,j) == end:
			res = longueur if longueur > res else res
			continue

		for (a,b) in g[(i,j)]:
			if (a,b) not in cache:
				new_longueur = longueur + g[(i,j)][(a,b)]
				Q.append((a,b,new_longueur,cache|{(a,b)}))
	return res

print("Partie 1 :",solve(1))
print("Partie 2 :",solve(2))