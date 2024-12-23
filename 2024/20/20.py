import time
START_TIME = time.time()

with open("input.txt") as f:
	texte = f.read().strip()

grid = [[j for j in i] for i in texte.splitlines()]
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == 'S':
			S = (i,j)
			break
	else:
		continue
	break

def shortcut(cheat):
	return [(dl,dc) for dl in range(-cheat,cheat+1) for dc in range(-cheat,cheat+1) if abs(dl)+abs(dc)<=cheat]

def dist(a,b):
	la,ca = a
	lb,cb = b
	return abs(la-lb)+abs(ca-cb)

def solve(cheat=2, time_saved=2):
	l,c = S
	N, M = len(grid), len(grid[0])
	dists = [[float("inf")]*len(grid[0]) for _ in range(len(grid))]
	dists[l][c] = 0
	while grid[l][c] != 'E':
		for nl,nc in [(l-1,c),(l+1,c),(l,c-1),(l,c+1)]:
			if 0<=nl<N and 0<=nc<M and grid[nl][nc] != '#':
				if dists[nl][nc] > dists[l][c]+1:
					dists[nl][nc] = dists[l][c]+1
					l,c = nl, nc
		
	SC = shortcut(cheat)
	res = 0
	for l in range(N):
		for c in range(M):
			for dl,dc in SC:
				nl, nc = l+dl, c+dc
				if 0<=nl<N and 0<=nc<M and grid[nl][nc] != '#':
					if dists[nl][nc]-(dists[l][c]+dist((l,c),(nl,nc))) >= time_saved:
						res += 1
	return res

print("Partie 1 :",solve(cheat=2, time_saved=100))
print("Partie 2 :",solve(cheat=20, time_saved=100))

# > 983968
print(f"[{int((time.time()-START_TIME)*1000)}ms]")