with open("input.txt") as f:
	texte = f.read()

# texte = """
# O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#...."""

grille = [[j for j in i] for i in texte.strip().splitlines()]

def affichage(grille):
	for i in grille:
		for j in i:
			print(j,end="")
		print()
	print()

def suivant(grille, facing):
	if facing == 0:
		for i in range(len(grille)):
			for j in range(len(grille[i])):
				if grille[i][j] == "O":
					current = i
					while current > 0 and grille[current-1][j] == '.':
						grille[current][j], grille[current-1][j] = grille[current-1][j], grille[current][j]
						current -= 1
	if facing == 1:
		for i in range(len(grille)):
			for j in range(len(grille[i])):
				if grille[i][j] == "O":
					current = j
					while current > 0 and grille[i][current-1] == '.':
						grille[i][current-1], grille[i][current] = grille[i][current], grille[i][current-1]
						current -= 1
	if facing == 2:
		for i in range(len(grille)-1,-1,-1):
			for j in range(len(grille[i])):
				if grille[i][j] == "O":
					current = i
					while current < len(grille)-1 and grille[current+1][j] == '.':
						grille[current][j], grille[current+1][j] = grille[current+1][j], grille[current][j]
						current += 1
	if facing == 3:
		for i in range(len(grille)):
			for j in range(len(grille[i])-1,-1,-1):
				if grille[i][j] == "O":
					current = j
					while current < len(grille[0])-1 and grille[i][current+1] == '.':
						grille[i][current+1], grille[i][current] = grille[i][current], grille[i][current+1]
						current += 1

def score(grille):
	res = 0
	for i in range(len(grille)):
		for j in range(len(grille[i])):
			if grille[i][j] == "O":
				res += len(grille) - i
	return res

suivant(grille,0)
print("Partie 1 :",score(grille))

grille = [[j for j in i] for i in texte.strip().splitlines()]

def deja_vu(cache, grille,cycle):
	for i in range(cycle-1, -1, -1):
		if cache[i] == grille:
			return cycle - i
	return 0

def part2():
	cache = dict()
	cache[0] = [[j for j in i] for i in grille]
	cycle = 1
	skip = False
	while cycle <= 1000000000:
		for facing in range(4):
			suivant(grille, facing)
		if not skip and deja_vu(cache, grille, cycle) != 0:
			x = deja_vu(cache, grille, cycle)
			cycle += x * ((1000000000 - cycle) // x)
			cache[cycle] = [[j for j in i] for i in grille]
			cycle += 1
			skip = True
		else:
			cache[cycle] = [[j for j in i] for i in grille]
			cycle += 1
	return score(grille)

print("Partie 2 :",part2())