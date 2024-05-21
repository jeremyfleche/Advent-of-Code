with open("input.txt") as f:
	texte = f.read()

# texte = """Tile 2311:
# ..##.#..#.
# ##..#.....
# #...##..#.
# ####.#...#
# ##.##.###.
# ##...#.###
# .#.#.#..##
# ..#....#..
# ###...#.#.
# ..###..###

# Tile 1951:
# #.##...##.
# #.####...#
# .....#..##
# #...######
# .##.#....#
# .###.#####
# ###.##.##.
# .###....#.
# ..#.#..#.#
# #...##.#..

# Tile 1171:
# ####...##.
# #..##.#..#
# ##.#..#.#.
# .###.####.
# ..###.####
# .##....##.
# .#...####.
# #.##.####.
# ####..#...
# .....##...

# Tile 1427:
# ###.##.#..
# .#..#.##..
# .#.##.#..#
# #.#.#.##.#
# ....#...##
# ...##..##.
# ...#.#####
# .#.####.#.
# ..#..###.#
# ..##.#..#.

# Tile 1489:
# ##.#.#....
# ..##...#..
# .##..##...
# ..#...#...
# #####...#.
# #..#.#.#.#
# ...#.#.#..
# ##.#...##.
# ..##.##.##
# ###.##.#..

# Tile 2473:
# #....####.
# #..#.##...
# #.##..#...
# ######.#.#
# .#...#.#.#
# .#########
# .###.#..#.
# ########.#
# ##...##.#.
# ..###.#.#.

# Tile 2971:
# ..#.#....#
# #...###...
# #.#.###...
# ##.##..#..
# .#####..##
# .#..####.#
# #..#.#..#.
# ..####.###
# ..#.#.###.
# ...#.#.#.#

# Tile 2729:
# ...#.#.#.#
# ####.#....
# ..#.#.....
# ....#..#.#
# .##..##.#.
# .#.####...
# ####.#.#..
# ##.####...
# ##..#.##..
# #.##...##.

# Tile 3079:
# #.#.#####.
# .#..######
# ..#.......
# ######....
# ####.#..#.
# .#...#.##.
# #.#####.##
# ..#.###...
# ..#.......
# ..#.###..."""

def affichage(grille):
	for i in grille:
		for j in i:
			print(j, end="")
		print()
	print()

def rotate(grille):
	res = [[] for i in grille]
	for i in range(len(grille)):
		for j in range(len(grille[i])):
			res[i].append(grille[j][i])
	return res

def bordure(side,grille):
	if side == "U":
		return grille[0]
	if side == "D":
		return grille[-1]
	if side == "R":
		return [grille[i][-1] for i in range(len(grille))]
	if side == "L":
		return [grille[i][0] for i in range(len(grille))]

def opose(side):
	if side == "U":
		return "D"
	if side == "D":
		return "U"
	if side == "R":
		return "L"
	if side == "L":
		return "R"

def coins(grille0):
	res = 0
	for _,grille in liste:
		if grille != grille0:
			temp = [i for i in grille]
			for side in ["U","D","R","L"]:
				temp = rotate(temp)
				for _ in range(4):
					if bordure(side,grille0) == bordure(opose(side),temp):
						res += 1
	return res


t = texte.strip().split("\n\n")
liste = []
for i in t:
	temp = i.splitlines()
	tuile = int(temp[0].split(" ")[1][:-1])
	grille = [[j for j in i] for i in temp[1:]]
	liste.append((tuile,grille))

for tuile,grille in liste:
	print(coins(grille))