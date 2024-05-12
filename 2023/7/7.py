with open("input.txt") as f:
	texte = f.read()

# texte = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""

t = [ligne.split() for ligne in texte.strip().splitlines()]

def meilleur(ligneA, ligneB):
	a = ligneA[0]
	b = ligneB[0]
	da = dict()
	db = dict()
	ordre = "AKQJT98765432"
	for i in range(5):
		da[a[i]] = da[a[i]]+1 if a[i] in da else 1
		db[b[i]] = db[b[i]]+1 if b[i] in db else 1
	powerA = list(reversed(sorted(da.values())))
	powerB = list(reversed(sorted(db.values())))
	for i in range(len(powerA)):
		if powerA[i] > powerB[i]:
			return True
		if powerA[i] < powerB[i]:
			return False
	for i in range(5):
		if ordre.index(a[i]) < ordre.index(b[i]):
			return True
		if ordre.index(a[i]) > ordre.index(b[i]):
			return False
	return True

def tri(t,version):
	if version == 1:
		for i in range(1,len(t)):
			j = i
			while j > 0 and meilleur(t[j-1],t[j]):
				t[j-1],t[j] = t[j],t[j-1]
				j -= 1
	else:
		for i in range(1,len(t)):
			j = i
			while j > 0 and meilleur2(t[j-1],t[j]):
				t[j-1],t[j] = t[j],t[j-1]
				j -= 1

tri(t,1)

res = 0
for i in range(len(t)):
	res += (i+1) * int(t[i][1])

print("Partie 1 :",res)

def meilleur2(ligneA, ligneB):
	a = ligneA[0]
	b = ligneB[0]
	da = dict()
	db = dict()
	ordre = "AKQT98765432J"
	compteurA = 0
	for i in range(5):
		if a[i] == "J":
			compteurA += 1
		else:
			da[a[i]] = da[a[i]]+1 if a[i] in da else 1
	compteurB = 0
	for i in range(5):
		if b[i] == "J":
			compteurB += 1
		else:
			db[b[i]] = db[b[i]]+1 if b[i] in db else 1
	powerA = list(reversed(sorted(da.values())))
	powerB = list(reversed(sorted(db.values())))
	if powerA != []:
		powerA[0] += compteurA
	else:
		powerA = [5]
	if powerB != []:
		powerB[0] += compteurB
	else:
		powerB = [5]
	for i in range(len(powerA)):
		try:
			if powerA[i] > powerB[i]:
				return True
			if powerA[i] < powerB[i]:
				return False
		except:
			return True
	for i in range(5):
		if ordre.index(a[i]) < ordre.index(b[i]):
			return True
		if ordre.index(a[i]) > ordre.index(b[i]):
			return False
	return True

tri(t,2)
res = 0
for i in range(len(t)):
	res += (i+1) * int(t[i][1])

print("Partie 2 :",res)