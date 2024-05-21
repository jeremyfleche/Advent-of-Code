with open("input.txt") as f:
	texte = f.read()

# texte = """.#.
# ..#
# ###"""

grille = [[[j for j in i] for i in texte.strip().splitlines()]]

cube = dict()
for z in range(len(grille)):
	for y in range(len(grille[z])):
		for x in range(len(grille[z][y])):
			if grille[z][y][x] == "#":
				cube[(z,y,x)] = 1

def dimensions(cube):
	x = [x for (z,y,x) in cube]
	y = [y for (z,y,x) in cube]
	z = [z for (z,y,x) in cube]
	return min(z),max(z),min(y),max(y),min(x),max(x)

def affichage(cube):
	minz,maxz,miny,maxy,minx,maxx = dimensions(cube)
	print("--------------------")
	for z in range(minz,maxz+1):
		for y in range(miny,maxy+1):
			for x in range(minx,maxx+1):
				print(('#' if (z,y,x) in cube else "."), end="")
			print()
		print(("--------------------") if z == maxz else "")

def nb_voisins(cube,z,y,x):
	res = 0
	for a in range(-1,2):
		for b in range(-1,2):
			for c in range(-1,2):
				if (z+a,y+b,x+c) in cube and (z+a,y+b,x+c) != (z,y,x):
					res += 1
	return res

def suivant(cube):
	minz,maxz,miny,maxy,minx,maxx = dimensions(cube)
	res = {a:b for a,b in cube.items()}
	for z in range(minz-1,maxz+2):
		for y in range(miny-1,maxy+2):
			for x in range(minx-1,maxx+2):
				if (z,y,x) in cube:
					if nb_voisins(cube,z,y,x) not in [2,3]:
						res.pop((z,y,x))
				else:
					if nb_voisins(cube,z,y,x) == 3:
						res[(z,y,x)] = 1
	return res

for _ in range(6):
	cube = suivant(cube)

print("Parties 1 :",sum(cube.values()))

#Partie 2

cube = dict()
for z in range(len(grille)):
	for y in range(len(grille[z])):
		for x in range(len(grille[z][y])):
			if grille[z][y][x] == "#":
				cube[(0,z,y,x)] = 1

def dimensions2(cube):
	x = [x for (w,z,y,x) in cube]
	y = [y for (w,z,y,x) in cube]
	z = [z for (w,z,y,x) in cube]
	w = [w for (w,z,y,x) in cube]
	return min(w),max(w),min(z),max(z),min(y),max(y),min(x),max(x)

def nb_voisins2(cube,w,z,y,x):
	res = 0
	for a in range(-1,2):
		for b in range(-1,2):
			for c in range(-1,2):
				for d in range(-1,2):
					if (w+a,z+b,y+c,x+d) in cube and (w+a,z+b,y+c,x+d) != (w,z,y,x):
						res += 1
	return res

def suivant2(cube):
	minw,maxw,minz,maxz,miny,maxy,minx,maxx = dimensions2(cube)
	res = {a:b for a,b in cube.items()}
	for w in range(minw-1,maxw+2):
		for z in range(minz-1,maxz+2):
			for y in range(miny-1,maxy+2):
				for x in range(minx-1,maxx+2):
					if (w,z,y,x) in cube:
						if nb_voisins2(cube,w,z,y,x) not in [2,3]:
							res.pop((w,z,y,x))
					else:
						if nb_voisins2(cube,w,z,y,x) == 3:
							res[(w,z,y,x)] = 1
	return res

for _ in range(6):
	cube = suivant2(cube)

print("Parties 2 :",sum(cube.values()))