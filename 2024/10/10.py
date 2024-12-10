with open("input.txt") as f:
	texte = f.read().strip()

# texte = """89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732"""

grid = [[int(j) for j in i] for i in texte.splitlines()]

def algo(i,j, cacheEnable=False):
	cache = (i,j)
	if grid[i][j] != 0:
		return 0
	cache = set()
	Q = [(i,j)]
	res = 0
	while Q:
		i,j = Q.pop()
		if cacheEnable and (i,j) in cache:
			continue
		cache.add((i,j))
		if grid[i][j] == 9:
			res += 1
			continue
		for a,b in [(-1,0),(1,0),(0,-1),(0,1)]:
			ni,nj = i+a, j+b
			if 0<=ni<len(grid) and 0<=nj<len(grid[0]) and grid[i][j]+1 == grid[ni][nj]:
				Q.append((ni, nj))
	return res

res1 = 0
res2 = 0
for i in range(len(grid)):
	for j in range(len(grid[i])):
		res1 += algo(i,j,True)
		res2 += algo(i,j)

print("Partie 1 :", res1)
print("Partie 2 :", res2)