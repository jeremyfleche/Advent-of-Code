with open("input.txt") as f:
	texte = f.read().strip()

temp1, temp2 = texte.split("\n\n")
grid = [[j for j in i] for i in temp1.splitlines()]
moves = [i for i in temp2.strip() if i!='\n']

for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == '@':
			l, c = i, j

def move(grid, l, c, direction):
	dl, dc = directions[direction]
	nl = l+dl
	nc = c+dc
	if grid[nl][nc] == 'O':
		move(grid, nl, nc, direction)
	if grid[nl][nc] == '.':
		grid[l][c], grid[nl][nc] = grid[nl][nc], grid[l][c]

def score():
	res = 0
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == 'O':
				res += i*100+j
	return res

directions = {'>': (0, 1), '<': (0, -1), 'v': (1, 0), '^': (-1, 0)}
def solve():
	global l, c
	for direction in moves:
		move(grid, l, c, direction)
		if grid[l][c] != '@':
			dl, dc = directions[direction]
			l += dl
			c += dc
	return score()

print("Partie 1 :",solve())

def changeLine(line):
	changes = {'#': "##", 'O': '[]', '.': '..', '@': '@.'}
	res = ""
	for i in line:
		res += changes[i]
	return res

grid = [[j for j in changeLine(i)] for i in temp1.splitlines()]
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == '@':
			l, c = i, j

def canMove(grid, l, c, direction):
	dl, dc = directions[direction]
	nl = l+dl
	nc = c+dc
	if grid[l][c] == '#':
		return False
	elif grid[nl][nc] in '[]':
		if direction in '<>':
			return canMove(grid, nl, nc, direction)
		else:
			if grid[nl][nc] == '[':
				return canMove(grid, nl, nc, direction) and canMove(grid, nl, nc+1, direction)
			else:
				return canMove(grid, nl, nc, direction) and canMove(grid, nl, nc-1, direction)
	return grid[nl][nc] == '.'

def move(grid, l, c, direction):
	dl, dc = directions[direction]
	nl = l+dl
	nc = c+dc
	if not canMove(grid, l, c, direction):
		pass
	else:
		if grid[nl][nc] in '[]':
			if direction in '<>':
				move(grid, nl, nc, direction)
			else:
				if grid[nl][nc] == '[':
					move(grid, nl, nc, direction)
					move(grid, nl, nc+1, direction)
				else:
					move(grid, nl, nc, direction)
					move(grid, nl, nc-1, direction)
		if grid[nl][nc] == '.':
			grid[l][c], grid[nl][nc] = grid[nl][nc], grid[l][c]

		if grid[nl][nc] == '.':
			grid[l][c], grid[nl][nc] = grid[nl][nc], grid[l][c]

def score():
	res = 0
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == '[':
				res += 100*i+j
	return res

print("Partie 2 :",solve())