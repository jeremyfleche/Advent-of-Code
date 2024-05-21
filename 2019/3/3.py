from math import inf

with open('input.txt','r') as f:
	texte = f.read()

fils = [[(ligne[0],int(ligne[1:])) for ligne in fil.strip().split(',')] for fil in texte.strip().split('\n')]

def affichage(d):
	minx = min([x for (x,y) in d])
	maxx = max([x for (x,y) in d])
	miny = min([y for (x,y) in d])
	maxy = max([y for (x,y) in d])
	for y in range(miny,maxy+1):
		for x in range(minx,maxx+1):
			try:
				print(d[(x,y)],end='')
			except:
				print('.',end='')
		print()


def trace_fil(instruction,fil):
	global liste
	global d
	global x
	global y
	global step
	for i in range(instruction[1]):
		if instruction[0] == 'U':
			step += 1
			y -= 1
			if (x,y) in d:
				d[(x,y)].add(fil)
			else:
				d[(x,y)] = {fil}
			liste[fil][(x,y)] = step
		if instruction[0] == 'D':
			step += 1
			y += 1
			if (x,y) in d:
				d[(x,y)].add(fil)
			else:
				d[(x,y)] = {fil}
			liste[fil][(x,y)] = step
		if instruction[0] == 'R':
			step += 1
			x += 1
			if (x,y) in d:
				d[(x,y)].add(fil)
			else:
				d[(x,y)] = {fil}
			liste[fil][(x,y)] = step
		if instruction[0] == 'L':
			step += 1
			x -= 1
			if (x,y) in d:
				d[(x,y)].add(fil)
			else:
				d[(x,y)] = {fil}
			liste[fil][(x,y)] = step

def distance_centre(x,y):
	return abs(x)+abs(y)

liste = [{},{}]
d = {(0,0):'o'}
for i in range(2):
	x,y = 0,0
	step = 0
	for instruction in fils[i]:
		trace_fil(instruction,i)

res1 = inf
res2 = inf
for (x,y) in d:
	if len(d[(x,y)]) == 2:
		if distance_centre(x,y) < res1:
			res1 = distance_centre(x,y)
		if liste[0][(x,y)] + liste[1][(x,y)] < res2:
			res2 = liste[0][(x,y)] + liste[1][(x,y)]
			
print('Partie 1 :',res1)
print('Partie 2 :',res2)