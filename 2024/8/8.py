with open("input.txt") as f:
	texte = f.read().strip()

grid = [[j for j in i] for i in texte.splitlines()]

antennas = set()
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] != '.':
			antennas.add((i,j))

E = set()
F = set()
for (i,j) in antennas:
	for (a,b) in antennas:
		if (i,j) == (a,b) or grid[i][j] != grid[a][b]:
			continue
		da = i-a
		db = j-b
		F.add((i,j))
		F.add((a,b))
		if 0<=a-da<len(grid) and 0<=b-db<len(grid[0]):
			E.add((a-da,b-db))
		while 0<=a-da<len(grid) and 0<=b-db<len(grid[0]):
			F.add((a-da,b-db))
			a -= da
			b -= db

print("Partie 1 :",len(E))
print("Partie 2 :",len(F))