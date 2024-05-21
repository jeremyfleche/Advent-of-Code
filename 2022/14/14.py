from math import inf

with open('input.txt','r') as f:
	texte = f.read()

t = [[[int(k) for k in j.strip().split(',')] for j in i.split('->')] for i in texte.split('\n') if i!='']

d = dict()
for ligne in t:
	for i in range(len(ligne)-1):
		x1,y1 = ligne[i]
		x2,y2 = ligne[i+1]
		for x in range(min(x1,x2),max(x1,x2)+1):
			for y in range(min(y1,y2),max(y1,y2)+1):
				d[(x,y)] = '#'

def plancher(d):
	max_y = 0
	for i in d.keys():
		x , y = i
		if y > max_y:
			max_y = y
	return max_y

def sable_dernier_couche(d,plancher):
	for i in d.keys():
		if plancher in i and d[i] == 'o':
			return True
	return False

def new_position(x,y,d):
	if (x,y+1) in d:
		if (x-1,y+1) not in d:
			return x-1,y+1
		elif (x+1,y+1) not in d:
			return x+1,y+1
		else:
			return x,y
	else:
		return (x,y+1)

plancher = plancher(d)
res = 0
while sable_dernier_couche(d,plancher) == False:
	x,y = 500,0
	while y < plancher:
		if (x,y) == new_position(x,y,d):
			break
		else:
			x,y = new_position(x,y,d)
	res += 1
	d[x,y] = 'o'

print('Partie 1 :',res-1)

def plancher2(d):
	max_y = 0
	for i in d.keys():
		x , y = i
		if y > max_y:
			max_y = y
	return max_y+2

d = dict()
for ligne in t:
	for i in range(len(ligne)-1):
		x1,y1 = ligne[i]
		x2,y2 = ligne[i+1]
		for x in range(min(x1,x2),max(x1,x2)+1):
			for y in range(min(y1,y2),max(y1,y2)+1):
				d[(x,y)] = '#'

plancher = plancher2(d)
res = 0
while (500,0) not in d:
	x,y = 500,0
	while y < plancher-1:
		if (x,y) == new_position(x,y,d):
			break
		else:
			x,y = new_position(x,y,d)
	res += 1
	d[x,y] = 'o'

print('Partie 2:',res) # Attendre environ 4 secondes pour le résultat