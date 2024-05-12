with open("input.txt") as f:
	texte = f.read()

# texte = """R 6 (#70c710)
# D 5 (#0dc571)
# L 2 (#5713f0)
# D 2 (#d2c081)
# R 2 (#59c680)
# D 2 (#411b91)
# L 5 (#8ceee2)
# U 2 (#caa173)
# L 1 (#1b58a2)
# U 2 (#caa171)
# R 2 (#7807d2)
# U 3 (#a77fa3)
# L 2 (#015232)
# U 2 (#7a21e3)"""

instructions = [(i.split()[0],int(i.split()[1])) for i in texte.strip().splitlines()]

def affichage(grille):
	for i in grille:
		for j in i:
			print(j,end='')
		print()
	print()

def bordure(liste):
	res = 0
	for i in range(len(liste)):
		x,y = liste[i]
		x1, y1 = liste[(i+1)%len(liste)]
		res += abs(x-x1) + abs(y-y1)
	return res


# Formule calculant l'aire d'un polygone à partir de la liste des coordonnées des sommets
#Sauf que l'aire calculée compte la moitié de la bordure
def aire(polygone):
	n = len(liste)
	res = 0
	for i in range(n):
		res += polygone[i][1] * (polygone[(i-1)%n][0] - polygone[(i+1)%n][0])
	return abs(res)//2

# On compte la bordure + l'aire du lagon sans les contour
def solve(liste):
	return bordure(liste) + (aire(liste) - bordure(liste)//2 + 1)

liste = []
x, y = 0, 0
for (di, v) in instructions:
	liste.append((x,y))
	if di == 'R':
		x += v
	elif di == 'L':
		x -= v
	elif di == 'D':
		y += v
	elif di == 'U':
		y -= v

print("Partie 1 :",solve(liste))

instructions = []

for ligne in texte.strip().splitlines():
	x = ligne.split()[-1][2:-2]
	temp = int(ligne.split()[-1][-2])
	if temp == 0:
		lettre = 'R'
	elif temp == 1:
		lettre = 'D'
	elif temp == 2:
		lettre = 'L'
	else:
		lettre = 'U'
	instructions.append((lettre, int(x,16)))

liste = []
x, y = 0, 0
for (di, v) in instructions:
	liste.append((x,y))
	if di == 'R':
		x += v
	elif di == 'L':
		x -= v
	elif di == 'D':
		y += v
	elif di == 'U':
		y -= v

print("Partie 2 :",solve(liste))