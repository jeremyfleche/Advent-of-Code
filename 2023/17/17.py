from heapq import heappush, heappop

with open("input.txt") as f:
	texte = f.read()

# texte = """2413432311323
# 3215453535623
# 3255245654254
# 3446585845452
# 4546657867536
# 1438598798454
# 4457876987766
# 3637877979653
# 4654967986887
# 4564679986453
# 1224686865563
# 2546548887735
# 4322674655533"""

poids = [[int(j) for j in i] for i in texte.strip().splitlines()]

def valide(i,j):
	return 0<=i<len(poids) and 0<=j<len(poids[0])

Q = [(0,0,0,0,0,0)]
cache = set()
while Q:
	(total,i,j,di,dj,n) = heappop(Q)

	if (i,j) == (len(poids)-1, len(poids[0])-1):
		print("Partie 1 :",total)
		break

	if not valide(i,j) or (i,j,di,dj,n) in cache:
		continue

	cache.add((i,j,di,dj,n))

	if n < 3:
		new_i = i+di
		new_j = j+dj
		if valide(new_i,new_j):
			heappush(Q, (total+poids[new_i][new_j], new_i, new_j, di, dj, n+1))

	for (new_di,new_dj) in {(0,-1),(0,1),(-1,0),(1,0)} - {(di, dj), (-di,-dj)}:
		new_i = i+new_di
		new_j = j+new_dj
		if valide(new_i,new_j):
			heappush(Q, (total+poids[new_i][new_j], new_i, new_j, new_di, new_dj, 1))

Q = [(0,0,0,0,0,0)]
cache = set()
while Q:
	(total,i,j,di,dj,n) = heappop(Q)

	if (i,j) == (len(poids)-1, len(poids[0])-1):
		print("Partie 2 :",total)
		break

	if not valide(i,j) or (i,j,di,dj,n) in cache:
		continue

	cache.add((i,j,di,dj,n))

	if n < 10:
		new_i = i+di
		new_j = j+dj
		if valide(new_i,new_j):
			heappush(Q, (total+poids[new_i][new_j], new_i, new_j, di, dj, n+1))

	if n > 3 or (di, dj) == (0,0):
		for (new_di,new_dj) in {(0,-1),(0,1),(-1,0),(1,0)} - {(di, dj), (-di,-dj)}:
			new_i = i+new_di
			new_j = j+new_dj
			if valide(new_i,new_j):
				heappush(Q, (total+poids[new_i][new_j], new_i, new_j, new_di, new_dj, 1))