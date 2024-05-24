def transfomation(image, code, current_infini_state):
	res = []
	couche = 2
	hauteur = len(image) + 2*couche
	largeur = len(image[0]) + 2*couche
	for i in range(hauteur):
		ligne = []
		for j in range(largeur):
			temp = ""
			for di in range(-1, 2):
				for dj in range(-1, 2):
					ni = i + di - couche
					nj = j + dj - couche
					if 0<=ni<len(image) and 0<=nj<len(image[0]):
						temp += "1" if image[ni][nj] == "#" else "0"
					else:
						temp += '0' if current_infini_state == "." else "1"
			ligne.append(code[int(temp,2)])
		res.append(ligne)
	if current_infini_state == "#":
		return res, code[-1]
	else:
		return res, code[0]

def pixels(image):
	return sum(ligne.count("#") for ligne in image)

def affichage(image):
	for i in image:
		for j in i:
			print(j, end="")
		print()
	print()

with open("input.txt") as f:
	texte = f.read().strip()

# texte = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
# #..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
# .######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
# .#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
# .#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
# ...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
# ..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

# #..#.
# #....
# ##..#
# ..#..
# ..###"""

code, image = texte.split("\n\n")
image = [[j for j in i.strip()] for i in image.splitlines()]
code = code.replace("\n", "")
current_infini_state = '.'
for i in range(1,51):
	image, current_infini_state = transfomation(image,code,current_infini_state)
	if i == 2:
		print("Partie 1 :", pixels(image))

print("Partie 2 :", pixels(image)) # attendre environ 12s