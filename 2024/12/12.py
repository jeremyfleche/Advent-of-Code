with open("input.txt") as f:
	texte = f.read().strip()

# texte = """RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE"""

grid = [[j for j in i ] for i in texte.splitlines()]


def sides(zone):
	res = 0
	for (i,j) in zone:
		R = (i,j+1) not in zone
		L =	(i,j-1) not in zone
		T = (i-1,j) not in zone
		B = (i+1,j) not in zone
		if T and R:
			res += 1
		if L and T:
			res += 1
		if B and L:
			res += 1
		if R and B:
			res += 1
		if not T and not R and (i-1,j+1) not in zone:
			res += 1
		if not L and not T and (i-1,j-1) not in zone:
			res += 1
		if not B and not L and (i+1,j-1) not in zone:
			res += 1
		if not R and not B and (i+1,j+1) not in zone:
			res += 1
	return res

def algo(grid):
	cache = set()
	res1 = 0
	res2 = 0
	for i in range(len(grid)):
		for j in range(len(grid)):
			if (i,j) in cache:
				continue
			area = 0
			perimeter = 0
			ch = grid[i][j]
			Q = [(i,j)]
			zone = set()
			while Q:
				a,b = Q.pop()
				zone.add((a,b))
				if (a,b) in cache:
					continue
				cache.add((a,b))
				area += 1
				for (c,d) in [(-1,0),(1,0),(0,-1),(0,1)]:
					na = a+c
					nb = b+d
					if 0<=na<len(grid) and 0<=nb<len(grid[0]) and grid[na][nb] == ch:
						Q.append((na,nb))
					else:
						perimeter += 1

			res1 += area*perimeter
			res2 += area*sides(zone)
			
	return res1, res2

res1, res2 = algo(grid)

print("Partie 1 :", res1)
print("Partie 2 :", res2)