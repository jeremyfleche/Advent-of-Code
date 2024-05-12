with open("input.txt") as f:
	texte = f.read()

# texte = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4"""

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

print(min(liste))

# Partie 2

seeds = [(seeds[i],seeds[i]+seeds[i+1]) for i in range(0, len(seeds), 2)]

for paquet in paquets:
	new_seeds = []
	while seeds:
		debut, fin = seeds.pop()
		trouve = False
		for a,b,c in paquet:
			i1 = max(debut,b)
			i2 = min(fin, b+c)
			if i1 < i2:
				new_seeds.append((i1 - b + a, i2 - b + a))
				if debut < i1:
					seeds.append((debut, i1))
				if i2 < fin:
					seeds.append((i2, fin))
				trouve = True
				break
		if not trouve:
			new_seeds.append((debut, fin))
	seeds = new_seeds

print(min(seeds)[0])