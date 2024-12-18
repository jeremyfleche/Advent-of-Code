with open("input.txt") as f:
	texte = f.read().strip()

# texte = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...
# """

M = [[j for j in i] for i in texte.splitlines()]

for i in range(len(M)):
	for j in range(len(M[i])):
		if M[i][j] in '^<>v':
			a,b = i,j

def createLoop(M, i, j, c, a, b):
	E = set()
	while 0<=i<len(M) and 0<=j<len(M[0]):
		if (i,j,c) in E:
			return True
		E.add((i,j,c))
		di, dj = offset[direction[c]]
		ni, nj = i+di, j+dj
		if 0>ni or ni>=len(M) or 0>nj or nj>=len(M[0]):
			return False
		if (ni,nj)==(a,b) or M[ni][nj] == '#':
			c = (c+1)%4
			continue
		i, j = ni, nj

cache = set()
res = 0
offset = {'^':(-1, 0), 'v':(1,0), '>':(0,1), '<':(0,-1)}
direction = '^>v<'
y,x = a,b
current = direction.index(M[y][x])
while 0<=y<len(M) and 0<=x<len(M[0]):
	cache.add((y,x))
	dy, dx = offset[direction[current]]
	ny, nx = y+dy, x+dx
	if 0>ny or ny>=len(M) or 0>nx or nx>=len(M[0]):
		break
	if M[ny][nx] == '#':
		current = (current+1)%4
		continue
	if (ny,nx) not in cache and createLoop(M,y,x,current, ny, nx):
		res += 1
	y, x = ny, nx

print("Partie 1 :", len(cache))
print("Partie 2 :", res)