from math import inf

with open("input.txt","r") as fichier:
	texte = fichier.read()

# texte = """1, 1
# 1, 6
# 8, 3
# 3, 4
# 5, 5
# 8, 9"""

t = [tuple(int(j) for j in i.split(",")) for i in texte.strip().split("\n")]

def man(a,b):
	xa, ya = a
	xb, yb = b
	return abs(xa-xb)+abs(ya-yb)

def plus_proche(point):
	liste = []
	for i in t:
		liste.append(man(i,point))
	return liste.index(min(liste))

minx = min([x for (x,y) in t])
maxx = max([x for (x,y) in t])
miny = min([y for (x,y) in t])
maxy = max([y for (x,y) in t])

d = dict()

for x in range(2*minx-maxx,2*maxx+minx+1):
	for y in range(2*miny-maxy,2*maxy+miny+1):
		d[(x,y)] = plus_proche((x,y))


def affiche():
	for x in range(2*minx-maxx,2*maxx+minx+1):
		for y in range(2*miny-maxy,2*maxy+miny+1):
			print(d[(x,y)],end=' ')
		print("\n",end='')

compteur = {i:0 for i in range(len(t))}

for x in range(2*minx-maxx,2*maxx+minx+1):
	for y in range(2*miny-maxy,2*maxy+miny+1):
		if x in {2*minx-maxx,2*maxx+minx} or y in {2*miny-maxy,2*maxy+miny}:
			compteur[d[(x,y)]] = inf
		else:
			compteur[d[(x,y)]] += 1

res = max([i for i in compteur.values() if i!=inf])
print(res)

#Partie 2

def valide(point):
	res = 0
	for i in t:
		res += man(point,i)
	return res < 10000

res = 0
for i in d:
	if valide(i):
		res += 1

print(res)