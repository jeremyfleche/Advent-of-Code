with open('input.txt','r') as f:
	texte = f.read()
"""
texte = '''# ######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#'''
"""

carte = [[j for j in i] for i in texte.strip().split('\n')]

def affichage(d):
	min_x = min([x for (x,y) in d])
	max_x = max([x for (x,y) in d])
	min_y = min([y for (x,y) in d])
	max_y = max([y for (x,y) in d])
	for y in range(min_y,max_y+1):
		for x in range(min_x,max_x+1):
			if isinstance(d[(x,y)],set):
				print(len(d[(x,y)]),end='')
			else:
				print(d[(x,y)],end='')
		print()
	print()

def points_accessibles(d,x,y):
	temp = {(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x,y)}
	res = set()
	for i in temp:
		try:
			if d[i] == ' ':
				res.add(i)
		except:
			pass
	return res

def mouv_blizzard(d,x,y):
	if d[(x,y)] == '>':
		x1,y1 = (x+1)%len(carte[0]),y
		while x1 == 0 or x1 == len(carte[0])-1:
			x1 = (x1+1)%len(carte[0])
		return x1,y1
	if d[(x,y)] == '<':
		x1,y1 = (x-1)%len(carte[0]),y
		while x1 == 0 or x1 == len(carte[0])-1:
			x1 = (x1-1)%len(carte[0])
		return x1,y1
	if d[(x,y)] == 'v':
		x1,y1 = x,(y+1)%len(carte)
		while y1 == 0 or y1 == len(carte)-1:
			y1 = (y1+1)%len(carte)
		return x1,y1
	if d[(x,y)] == '^':
		x1,y1 = x,(y-1)%len(carte)
		while y1 == 0 or y1 == len(carte)-1:
			y1 = (y1-1)%len(carte)
		return x1,y1

def ajoute_new(new,x1,y1,i):
	try:
		if isinstance(new[(x1,y1)],set):
			new[(x1,y1)].add(i)
		else:
			new[(x1,y1)] = set(new[(x1,y1)])
			new[(x1,y1)].add(i)
	except:
		new[(x1,y1)] = i

def blizzard(d):
	new = dict()
	for (x,y) in d:
		if isinstance(d[(x,y)],set):
			for i in d[(x,y)]:
				if i == '>':
					x1,y1 = (x+1)%len(carte[0]),y
					while x1 == 0 or x1 == len(carte[0])-1:
						x1 = (x1+1)%len(carte[0])
					ajoute_new(new,x1,y1,i)
				if i == '<':
					x1,y1 = (x-1)%len(carte[0]),y
					while x1 == 0 or x1 == len(carte[0])-1:
						x1 = (x1-1)%len(carte[0])
					ajoute_new(new,x1,y1,i)
				if i == 'v':
					x1,y1 = x,(y+1)%len(carte)
					while y1 == 0 or y1 == len(carte)-1:
						y1 = (y1+1)%len(carte)
					ajoute_new(new,x1,y1,i)
				if i == '^':
					x1,y1 = x,(y-1)%len(carte)
					while y1 == 0 or y1 == len(carte)-1:
						y1 = (y1-1)%len(carte)
					ajoute_new(new,x1,y1,i)

		elif d[(x,y)] in {'>','<','v','^'}:
			x1,y1 = mouv_blizzard(d,x,y)
			try:
				if isinstance(new[(x1,y1)],set):
					new[(x1,y1)].add(d[(x,y)])
				else:
					new[(x1,y1)] = set(new[(x1,y1)])
					new[(x1,y1)].add(d[(x,y)])
			except:
				new[(x1,y1)] = d[(x,y)]
	for (x,y) in d:
		if (x,y) not in new:
			if x == 0 or x == len(carte[0])-1 or y == 0 or y == len(carte)-1:
				new[(x,y)] = d[(x,y)]
			else:
				new[(x,y)] = ' '
	return new

d = dict()
for y in range(len(carte)):
	for x in range(len(carte[y])):
		if carte[y][x] != '.':
			d[(x,y)] = carte[y][x]
		else:
			d[(x,y)] = ' '

#affichage(d)

minutes = 0
Q = {(1,0)}
while True:
	d = blizzard(d)
	temp = {i for i in Q}
	for (x,y) in Q:
		temp.remove((x,y))
		for i in points_accessibles(d,x,y):
			temp.add(i)
	Q = {i for i in temp}
	minutes += 1
	#print(minutes)
	#affichage(d)
	if (len(carte[0])-2,len(carte)-1) in Q:
		break

print('Partie 1 :',minutes)

Q = {(len(carte[0])-2,len(carte)-1)}
while True:
	d = blizzard(d)
	temp = {i for i in Q}
	for (x,y) in Q:
		temp.remove((x,y))
		for i in points_accessibles(d,x,y):
			temp.add(i)
	Q = {i for i in temp}
	minutes += 1
	#print(minutes)
	#affichage(d)
	if (1,0) in Q:
		break

Q = {(1,0)}
while True:
	d = blizzard(d)
	temp = {i for i in Q}
	for (x,y) in Q:
		temp.remove((x,y))
		for i in points_accessibles(d,x,y):
			temp.add(i)
	Q = {i for i in temp}
	minutes += 1
	#print(minutes)
	#affichage(d)
	if (len(carte[0])-2,len(carte)-1) in Q:
		break

print('Partie 2 :',minutes)