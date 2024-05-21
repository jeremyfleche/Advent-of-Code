with open('input.txt','r') as f:
	texte = f.read()
"""
texte = '''....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..'''
"""
grille = [[j for j in i] for i in texte.strip().split('\n')]

orientation = ['N','S','O','E']

def neighbor(x,y):
	voisins = {'N':0, 'S':0, 'E':0, 'O':0, 'NE':0, 'SE':0, 'SO': 0, 'NO':0}
	if (x-1,y-1) in d:
		if d[(x-1,y-1)] == 1:
			voisins['NO'] = 1
	if (x,y-1) in d:
		if d[(x,y-1)] == 1:
			voisins['N'] = 1
	if (x+1,y-1) in d:
		if d[(x+1,y-1)] == 1:
			voisins['NE'] = 1
	if (x-1,y) in d:
		if d[(x-1,y)] == 1:
			voisins['O'] = 1
	if (x+1,y) in d:
		if d[(x+1,y)] == 1:
			voisins['E'] = 1
	if (x-1,y+1) in d:
		if d[(x-1,y+1)] == 1:
			voisins['SO'] = 1
	if (x,y+1) in d:
		if d[(x,y+1)] == 1:
			voisins['S'] = 1
	if (x+1,y+1) in d:
		if d[(x+1,y+1)] == 1:
			voisins['SE'] = 1
	return voisins

def mouv(pointeur,x,y):
	res = ''
	voisins = neighbor(x,y)
	i = 0
	while i <= 3:
		facing = orientation[(pointeur+i)%4]
		temp = [i for i in voisins if facing in i]
		if all(voisins[x] == 0 for x in temp):
			return facing
		i += 1

def destination(pointeur,x,y):
	voisins = neighbor(x,y)
	if all(voisins[x]==0 for x in voisins):
		return None
	facing = mouv(pointeur,x,y)
	if facing == 'N':
		return x,y-1
	if facing == 'S':
		return x,y+1
	if facing == 'E':
		return x+1,y
	if facing == 'O':
		return x-1,y

def provenant(x,y):
	provenants = {(x,y-1),(x-1,y),(x+1,y),(x,y+1)}
	res = set()
	for i in provenants:
		try:
			if d[i] == 1:
				res.add(i)
		except:
			pass
	return res

def affichage(d,x1,x2,y1,y2):
	for y in range(x1,x2+1):
		for x in range(y1,y2+1): 
			if d[(x,y)] == 1:
				print('#',end='')
			else:
				print('.',end='')
		print()

d = dict()
for y in range(-10,len(grille)+10):
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

tour = 0
while tour < 10:
	new = dict()
	for (x,y) in d:
		if d[(x,y)] == 1 and destination(tour,x,y) == None:
			new[(x,y)] = 1
		elif d[(x,y)] == 0:
			provenants = provenant(x,y)
			viennent = []
			for (i,j) in provenants:
				if destination(tour,i,j) == (x,y):
					viennent.append((i,j))
			if len(viennent) == 1:
				i,j = viennent[0]
				new[(x,y)] = 1
				new[(i,j)] = 0
			else:
				for (i,j) in viennent:
					new[(i,j)] = 1
				new[(x,y)] = 0
	d = new
	tour += 1	

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

d = dict()
for y in range(-len(grille),2*len(grille)):
	for x in range(-len(grille[0]),2*len(grille[0])):
		try:
			if grille[y][x] == '#':
				d[(x,y)] = 1
			else:
				d[(x,y)] = 0
		except:
			d[(x,y)] = 0

tour = 0
while True:
	new = dict()
	for (x,y) in d:
		if d[(x,y)] == 1 and destination(tour,x,y) == None:
			new[(x,y)] = 1
		elif d[(x,y)] == 0:
			provenants = provenant(x,y)
			viennent = []
			for (i,j) in provenants:
				if destination(tour,i,j) == (x,y):
					viennent.append((i,j))
			if len(viennent) == 1:
				i,j = viennent[0]
				new[(x,y)] = 1
				new[(i,j)] = 0
			else:
				for (i,j) in viennent:
					new[(i,j)] = 1
				new[(x,y)] = 0
	tour += 1
	print('tour :',tour)
	if new == d:
		break
	d = new

print('Partie 2 :',tour) # cela prend 5 min car pas optimisé