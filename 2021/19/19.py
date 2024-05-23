def orientations(scanner):
	res = [set() for _ in range(24)]
	for x,y,z in scanner:
		temp = []

		# z positif
		temp.append((x,y,z))
		temp.append((y,-x,z))
		temp.append((-x,-y,z))
		temp.append((-y,x,z))
		
		# z négatif
		temp.append((-x,y,-z))
		temp.append((-y,-x,-z))
		temp.append((x,-y,-z))
		temp.append((y,x,-z))

		# x positif
		temp.append((-z,y,x))
		temp.append((y,z,x))
		temp.append((z,-y,x))
		temp.append((-y,-z,x))

		# x négatif
		temp.append((z,y,-x))
		temp.append((y,-z,-x))
		temp.append((-z,-y,-x))
		temp.append((-y,z,-x))

		# y positif
		temp.append((x,-z,y))
		temp.append((-z,-x,y))
		temp.append((-x,z,y))
		temp.append((z,x,y))

		# y négatif
		temp.append((-x,-z,-y))
		temp.append((-z,x,-y))
		temp.append((x,z,-y))
		temp.append((z,-x,-y))

		for i in range(24):
			res[i].add(temp[i])
	return res

def bonne_orientation(i):
	for orientation in orientations(scanners[i]):
		for j in range(len(new_scanners)):
			for xo,yo,zo in orientation:
				for x,y,z in new_scanners[j]:
					dx = x - xo
					dy = y - yo
					dz = z - zo
					temp = {(xo+dx,yo+dy,zo+dz) for (xo,yo,zo) in orientation}
					if len(new_scanners[j] & temp) >= 12:
						print(f"Scanner {i} trouvé !")
						position_scanners.append((dx,dy,dz))
						return temp

with open("input.txt") as f:
	texte = f.read().strip()

scanners = [set(tuple(int(i) for i in ligne.split(",")) for ligne in scanner.splitlines()[1:]) for scanner in texte.split("\n\n")]

beacons = {i for i in scanners[0]}
scanners_bien_orientes = [scanners[0]]
new_scanners = [scanners[0]]
pas_encore_trouves = set(range(1,len(scanners)))
position_scanners = [(0,0,0)]

while pas_encore_trouves:
	infini = True
	scanners_bien_orientes = []
	news_scanners_indice = set()
	for i in pas_encore_trouves:
		E = bonne_orientation(i)
		if E != None:
			news_scanners_indice.add(i)
			scanners_bien_orientes.append(E)
			beacons |= E
	pas_encore_trouves -= news_scanners_indice
	new_scanners = [i for i in scanners_bien_orientes]

print("Partie 1 :",len(beacons)) # attendre environ 43s

res = 0
for a,b,c in position_scanners:
	for d,e,f in position_scanners:
		res = max(abs(a-d)+abs(b-e)+abs(c-f), res)

print("Partie 2 :",res)