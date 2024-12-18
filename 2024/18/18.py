import time
t = time.time()

with open("input.txt") as f:
	texte = f.read().strip()

def affichage(grid, stop):
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			print(grid[y][x] if (x,y) != stop else 'X', end="")
		print()
	print()

def init(s):
	d = {}
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			d[(i,j)] = float("inf")
	d[s] = 0
	return d

def selectMin(Q,d):
	val = float("inf")
	for (i,j) in Q:
		if d[(i,j)] < val:
			res = (i,j)
			val = d[(i,j)]
	return (i,j)

def part1(grid, C):
	for (x,y) in C[:1024]:
		grid[y][x] = '#'
	s = (0,0)
	d = init(s)
	Q = {s}
	while Q:
		l,c = selectMin(Q, d)
		Q.discard((l,c))
		for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
			nl = l+i
			nc = c+j
			if 0<=nl<len(grid) and 0<=nc<len(grid[0]) and grid[nl][nc] != '#':
				if d[(l,c)] + 1 < d[(nl,nc)]:
					d[(nl,nc)] = d[(l,c)] + 1
					Q.add((nl,nc))
	
	return d[(len(grid)-1,len(grid[0])-1)]

def is_accessible(grid):
	cache = set()
	Q = [(0,0)]
	while Q:
		l,c = Q.pop()
		if (l,c) == (len(grid)-1,len(grid[0])-1):
			return True
		if (l,c) in cache:
			continue
		cache.add((l,c))
		for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
			nl = l+i
			nc = c+j
			if 0<=nl<len(grid) and 0<=nc<len(grid[0]) and grid[nl][nc] != '#':
				Q.append((nl,nc))
	return False

def part2(grid, C):
	for (x,y) in C[:1024]:
		grid[y][x] = '#'
	k = 1023
	while is_accessible(grid):
		k += 1
		x,y = C[k]
		grid[y][x] = '#'
	return ','.join([str(i) for i in C[k]])

grid = grid = [['.']*71 for _ in range(71)]
C = [tuple(map(int, i.split(','))) for i in texte.splitlines()]

print("Partie 1 :", part1(grid, C))
print("Partie 2 :", part2(grid, C))
# print(is_accessible(grid))
print(f"[{int((time.time()-t)*1000)}ms]")