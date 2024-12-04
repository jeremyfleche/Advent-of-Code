with open("input.txt") as f:
	t = f.read().strip().splitlines()

offsets = []
for i in range(-1,2):
	for j in range(-1, 2):
		if (i,j) != (0,0):
			offsets.append((i,j))

res1 = 0
mot = "XMAS"
for i in range(len(t)):
	for j in range(len(t[i])):
		if t[i][j] == 'X':
			Q = []
			for offset in offsets:
				Q.append((0, i, j, offset))
			while Q:
				p, a, b, (da, db) = Q.pop()
				if p == 3:
					res1 += 1
					continue
				if 0<=a+da<len(t) and 0<=b+db<len(t[0]) and t[a+da][b+db] == mot[p+1]:
					Q.append((p+1, a+da, b+db, (da,db)))

print("Partie 1 :",res1)

res2 = 0
for i in range(1, len(t)-1):
	for j in range(1, len(t[i])-1):
		if t[i][j] == 'A':
			if t[i-1][j-1] == 'M' and t[i+1][j-1] == 'M' and t[i+1][j+1] == 'S' and t[i-1][j+1] == 'S':
				res2 += 1
			elif t[i-1][j-1] == 'M' and t[i-1][j+1] == 'M' and t[i+1][j+1] == 'S' and t[i+1][j-1] == 'S':
				res2 += 1
			elif t[i+1][j-1] == 'M' and t[i+1][j+1] == 'M' and t[i-1][j-1] == 'S' and t[i-1][j+1] == 'S':
				res2 += 1
			elif t[i+1][j+1] == 'M' and t[i-1][j+1] == 'M' and t[i-1][j-1] == 'S' and t[i+1][j-1] == 'S':
				res2 += 1

print("Partie 2 :",res2)