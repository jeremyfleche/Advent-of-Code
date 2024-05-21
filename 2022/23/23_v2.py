with open('input.txt','r') as f:
	texte = f.read()

texte = '''....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..'''

grille = [[j for j in i] for i in texte.strip().split('\n')]

orientation = ['N','S','O','E']

def affichage(d):
	min_x = min([x for (x,y) in d if d[(x,y)]==1])
	max_x = max([x for (x,y) in d if d[(x,y)]==1])
	min_y = min([y for (x,y) in d if d[(x,y)]==1])
	max_y = max([y for (x,y) in d if d[(x,y)]==1])
	for y in range(min_y,max_y+1):
		for x in range(min_x,max_x+1): 
			if d[(x,y)] == 1:
				print('#',end='')
			else:
				print('.',end='')
		print()

d = dict()
for y in range(len(grille)):
	for x in range(-10,len(grille[0])+10):
		if x<0 or y<0:
			d[(x,y)] = 0
		else:
			try:
				if grille[y][x] == '#':
					d[(x,y)] = 1
				else:
					d[(x,y)] = 0
			except:
				d[(x,y)] = 0

def position_suivante_facing(facing,x,y):
	if facing == 'N':
		return x,y-1
	elif facing == 'S':
		return x,y+1
	elif facing == 'O':
		return x-1,y
	else:
		return x+1,y

def bouge_pas(d,x,y):
	voisins = {(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)}
	for (x,y) in voisins:
		try:
			if d[(x,y)] == '#':
				return False
		except:
			pass
	return True

def position_suivante(d,tour,x,y):
	if bouge_pas(d,x,y):
		return x,y
	i = 0
	while i<4:
		facing = orientation[(tour+1)%4]
		x1,y1 = position_suivante_facing(facing,x,y)
		try:
			if d[(x1,y1)] == '#':
				pass
			else:
				return x1,y1
		except:
			return x1,y1
		i += 1
	return x,y

tour = 0
while True:
	new = {}
	destination = {}
	rep_destination = {}
	for (x,y) in d:
		if d[(x,y)] == 1:
			x1,y1 = position_suivante(d,tour,x,y)
			if (x,y) == (x1,y1):
				new[(x,y)] = 1
			else:
				destination[(x,y)] = (x1,y1)
				try:
					rep_destination[(x1,y1)] += 1
				except:
					rep_destination[(x1,y1)] = 1
		else:
			new[(x,y)] = 0
	for (x,y) in destination:
		if rep_destination[destination[(x,y)]] == 1:
			new[destination[(x,y)]] = 1
		else:
			new[destination[(x,y)]] = 0 

	tour += 1
	if tour == 10:
		min_x = min([x for (x,y) in d if d[(x,y)]==1])
		max_x = max([x for (x,y) in d if d[(x,y)]==1])
		min_y = min([y for (x,y) in d if d[(x,y)]==1])
		max_y = max([y for (x,y) in d if d[(x,y)]==1])
		res = 0
		for x in range(min_x,max_x+1):
			for y in range(min_y,max_y+1):
				if d[(x,y)] == 0:
					res += 1
		print('Partie 1 :',res)
	affichage(new)
	if d == new:
		print('Partie 2 :',tour)
		break
	d = new

print("\n-----------------\nNE FONCTIONNE PAS\n-----------------\n")
