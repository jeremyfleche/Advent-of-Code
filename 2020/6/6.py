with open("input.txt") as f:
	texte = f.read()

t = [i.split("\n") for i in texte.strip().split("\n\n")]

def compte(lettre,d):
	for i in d:
		if lettre not in d[i]:
			return False
	return True

res1 = 0
res2 = 0
for group in t:
	E = set()
	d = dict()
	for person in range(len(group)):
		for lettre in group[person]:
			E.add(lettre)
			try:
				d[person] += lettre
			except:
				d[person] = lettre
	for lettre in E:
		if compte(lettre,d):
			res2 += 1
	res1 += len(E)

print("Partie 1 :",res1)
print("Partie 1 :",res2)