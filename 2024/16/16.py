with open("input.txt") as f:
	texte = f.read().strip()

# texte = """#################
# #...#...#...#..E#
# #.#.#.#.#.#.#.#.#
# #.#.#.#...#...#.#
# #.#.#.#.###.#.#.#
# #...#.#.#.....#.#
# #.#.#.#.#.#####.#
# #.#...#.#.#.....#
# #.#.#####.#.###.#
# #.#.#.......#...#
# #.#.###.#####.###
# #.#.#...#.....#.#
# #.#.#.#####.###.#
# #.#.#.........#.#
# #.#.#.#########.#
# #S#.............#
# #################"""

def init(grid):
	d = {}
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			for x in range(4):
				if grid[i][j] != '#':
					d[((i,j),x)] = float("inf")
				if grid[i][j] == 'S':
					s = (i,j)
				if grid[i][j] == 'E':
					e = (i,j)
	d[(s,0)] = 0
	return s, e, d

def selectMin(Q, d):
	val = float("inf")
	for x in Q:
		if d[x] < val:
			res = x
			val = d[x]
	return res

def getMin(d,e):
	res = float("inf")
	for i in range(4):
		res = min(res, d.get((e,i), float("inf")))
	return res

def affichage(cache):
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			print('O' if (i,j) in cache else grid[i][j], end="")
		print()

def part2(S, s, e, d):
	res = set()
	directions = [(0,1), (-1,0), (0,-1), (1,0)] # est, nord, ouest, sud
	Q = [(s,0,0, set())]
	while Q:
		(l,c), Dir, score, C = Q.pop()
		C |= {(l,c)}
		if grid[l][c] == 'E' and score == S:
			res |= C
			continue
		if score > d[((l,c),Dir)]:
			continue
		Q.append(((l,c), (Dir-1)%4, score+1000, {i for i in C}))
		Q.append(((l,c), (Dir+1)%4, score+1000, {i for i in C}))
		i,j = directions[Dir]
		nl, nc = l+i, c+j
		if grid[nl][nc] == '#':
			continue
		Q.append(((nl,nc), Dir, score+1, {i for i in C}))

	return len(res)

def algo(grid):
	s, e, d = init(grid)
	directions = [(0,1), (-1,0), (0,-1), (1,0)]
	Q = {(s,0)}
	while Q:
		(l,c), Dir = selectMin(Q, d)
		Q.discard(((l,c), Dir))
		i,j = directions[Dir]
		nl, nc = l+i, c+j
		rotate = d[((l,c),Dir)] + 1000
		if d[((l,c),(Dir-1)%4)] >= rotate:
			d[((l,c),(Dir-1)%4)] = rotate
			Q.add(((l,c), (Dir-1)%4))
		if d[((l,c),(Dir+1)%4)] >= rotate:
			d[((l,c),(Dir+1)%4)] = rotate
			Q.add(((l,c), (Dir+1)%4))
		if grid[nl][nc] == '#':
			continue
		if d[((nl,nc),Dir)] >= d[((l,c),Dir)] + 1:
			d[((nl,nc),Dir)] = d[((l,c),Dir)] + 1
			Q.add(((nl,nc), Dir))

	res1 = getMin(d,e)
	return res1, part2(res1, s, e, d)

grid = [[j for j in i] for i in texte.splitlines()]
res1, res2 = algo(grid)
print("Partie 1 :", res1)
print("Partie 2 :", res2)