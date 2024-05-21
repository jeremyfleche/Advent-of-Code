with open('input.txt','r') as f:
	texte = f.read()

texte = texte.split('\n\n')

def nombre(temp):
	if temp.isdigit():
		return int(temp)
	return temp

instructions = []
temp = ''
for i in texte[1]:
	if temp!='' and temp[-1].isdigit() != i.isdigit():
		instructions.append(nombre(temp))
		temp = i
	else:
		temp += i

if temp!='' and temp!='\n':
	instructions.append(nombre(temp))


grille = [[' ' if j==' ' else j for j in i] for i in texte[0].split('\n')]

for ligne in range(len(grille)):
	for i in range(max([len(grille[i]) for i in range(len(grille))])-len(grille[ligne])):
		grille[ligne].append(' ')
"""
for i in grille:
	for j in i:
		print(j,end='')
	print()
"""

def affichage(grille):
	for i in grille:
		for j in i:
			print(j,end='')
		print()

def move(x,y,facing):
	if facing == 'est':
		return ((x+1)%len(grille[0]),y)
	elif facing == 'sud':
		return (x,(y+1)%len(grille))
	elif facing == 'ouest':
		return ((x-1)%len(grille[0]),y)
	else:
		return (x,(y-1)%len(grille))

pointeur = 0
orientation = ['est','sud','ouest','nord']
facing = orientation[pointeur]
x,y = 0,0
for instruction in instructions:
	if isinstance(instruction,int):
		for _ in range(instruction):
			x1,y1 = move(x,y,facing)
			while grille[y1][x1] == ' ':
				x1,y1 = move(x1,y1,facing)
			if grille[y1][x1] == '#':
				break
			else:
				x,y = x1,y1
	else:
		if instruction == 'R':
			pointeur = (pointeur+1)%4
			facing = orientation[pointeur]
		else:
			pointeur = (pointeur-1)%4
			facing = orientation[pointeur]

print('Partie 1 :',1000*(y+1)+4*(x+1)+pointeur)

# Partie 2

dimensions = len(grille)//4

def face(x,y):
	global dimensions
	if x < dimensions:
		if 2*dimensions <= y < 3*dimensions:
			return 4
		else:
			return 6
	elif dimensions <= x < 2*dimensions:
		if y < dimensions:
			return 1
		elif dimensions <= y < 2*dimensions:
			return 3
		else:
			return 5
	else:
		return 2

def hors_grille(x,y):
	global grille
	if x>=len(grille[0]) or x<0 or y>=len(grille) or y<0:
		return True
	return False

def face_suivante(x,y):
	global facing
	global dimensions
	global pointeur
	global orientation
	if facing == 'est':
		if face(x,y) == 1:
			return x+1,y
		if face(x,y) == 2:
			pointeur = 2
			facing = orientation[pointeur]
			return 2*dimensions-1,3*dimensions-y-1
		if face(x,y) == 3:
			pointeur = 3
			facing = orientation[pointeur]
			return y+dimensions,dimensions-1
		if face(x,y) == 4:
			return x+1,y
		if face(x,y) == 5:
			pointeur = 2
			facing = orientation[pointeur]
			return 3*dimensions-1,3*dimensions-y-1
		if face(x,y) == 6:
			pointeur = 3
			facing = orientation[pointeur]
			return y-2*dimensions,3*dimensions-1
	if facing == 'sud':
		if face(x,y) == 1:
			return x,y+1
		if face(x,y) == 2:
			pointeur = 2
			facing = orientation[pointeur]
			return 2*dimensions-1,x-dimensions
		if face(x,y) == 3:
			return x,y+1
		if face(x,y) == 4:
			return x,y+1
		if face(x,y) == 5:
			pointeur = 2
			facing = orientation[pointeur]
			return dimensions-1,x+2*dimensions
		if face(x,y) == 6:
			return x+2*dimensions,0
	if facing == 'ouest':
		if face(x,y) == 1:
			pointeur = 0
			facing = orientation[pointeur]
			return 0,3*dimensions-y-1
		if face(x,y) == 2:
			return x-1,y
		if face(x,y) == 3:
			pointeur = 1
			facing = orientation[pointeur]
			return y-dimensions,2*dimensions
		if face(x,y) == 4:
			pointeur = 0
			facing = orientation[pointeur]
			return dimensions,3*dimensions-y-1
		if face(x,y) == 5:
			return x-1,y
		if face(x,y) == 6:
			pointeur = 1
			facing = orientation[pointeur]
			return y-2*dimensions,0
	if facing == 'nord':
		if face(x,y) == 1:
			pointeur = 0
			facing = orientation[pointeur]
			return 0,x+2*dimensions
		if face(x,y) == 2:
			return x-2*dimensions,4*dimensions-1
		if face(x,y) == 3:
			return x,y-1
		if face(x,y) == 4:
			pointeur = 0
			facing = orientation[pointeur]
			return dimensions,x+dimensions
		if face(x,y) == 5:
			return x,y-1
		if face(x,y) == 6:
			return x,y-1

def move2(x,y,facing):
	if facing == 'est':
		return (x+1,y)
	elif facing == 'sud':
		return (x,y+1)
	elif facing == 'ouest':
		return (x-1,y)
	else:
		return (x,y-1)

def graphisme(facing):
	if facing == 'est':
		return '>'
	elif facing == 'sud':
		return 'v'
	elif facing == 'ouest':
		return '<'
	else:
		return '^'

pointeur = 0
orientation = ['est','sud','ouest','nord']
facing = orientation[pointeur]
x,y = dimensions,0
grille[y][x] = 'X'
for instruction in instructions:
	if isinstance(instruction,int):
		for _ in range(instruction):
			x1,y1 = move2(x,y,facing)
			if hors_grille(x1,y1):
				old_pointeur = pointeur
				x1, y1 = face_suivante(x,y)
				if grille[y1][x1] == '#':
					pointeur = old_pointeur
					facing = orientation[pointeur]
					break
				else:
					x,y = x1,y1
			elif grille[y1][x1] == ' ':
				old_pointeur = pointeur
				x1, y1 = face_suivante(x,y)
				if grille[y1][x1] == '#':
					pointeur = old_pointeur
					facing = orientation[pointeur]
					break
				else:
					x,y = x1,y1
			elif grille[y1][x1] == '#':
				break
			else:
				x,y = x1,y1
			grille[y][x] = graphisme(facing)
	else:
		if instruction == 'R':
			pointeur = (pointeur+1)%4
			facing = orientation[pointeur]
		else:
			pointeur = (pointeur-1)%4
			facing = orientation[pointeur]
	grille[y][x] = graphisme(facing)

print('Partie 2 :',1000*(y+1)+4*(x+1)+pointeur) 
#affichage(grille)
