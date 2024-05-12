with open("input.txt") as f:
	texte = f.read()

seeds = [int(i) for i in texte.split("\n\n")[0].split()[1:]]
paquets = [[[int(k) for k in j.split()] for j in i.splitlines()[1:]] for i in texte.split("\n\n")[1:]]

liste = []
for x in seeds:
	for paquet in paquets:
		for a,b,c in paquet:
			if b <= x < b+c:
				x = x - (b - a)
				break
	liste.append(x)

print("Partie 1 :",min(liste))

# Partie 2

seeds = [(seeds[i],seeds[i]+seeds[i+1]) for i in range(0, len(seeds), 2)]

for paquet in paquets:											# Pour chaque transformation (send-to-soil, soil-to-fertilizer, ...)
	new_seeds = []
	while seeds:												# Tant qu'on a pas traité tous les intervalles
		debut, fin = seeds.pop()
		trouve = False											# Variable pour savoir à la fin de la transformation si on a trouvé une intersection avec une ligne
		for a,b,c in paquet:									# Pour chaque a,b,c (destination, source, range)
			i1 = max(debut,b)									# (i1, i2) correspond à l'intervalle d'intersection entre (debut, fin) et (b, b+c)
			i2 = min(fin, b+c)
			if i1 < i2:											# Si l'intersection n'est pas vide
				new_seeds.append((i1 - b + a, i2 - b + a))		# On ajoute à la nouvelle liste la transformation de (i1, i2)
				if debut < i1:									# S'il y a des valeurs dans (debut, fin) avant i1
					seeds.append((debut, i1))					# On le rajoute à seeds pour trouver une transformation (s'il y en a une sinon on le rajoutera tel quel ligne 39
				if i2 < fin:									# Pareil s'il y a des valeurs dans (début, fin) après i2
					seeds.append((i2, fin))
				trouve = True									# Vu qu'on a trouvé un intervalle
				break
		if not trouve:											# Si on a pas trouvé de correspondance avec un intervalle
			new_seeds.append((debut, fin))						# On le rajoute tel quel
	seeds = new_seeds											# On réaffecte à seeds les intervalles découpés et/ou transformés

print("Partie 2 :",min(seeds)[0])