with open("input.txt") as f:
	texte = f.read().strip()

liste = [i.split(")") for i in texte.splitlines()]
orbites = dict()
for a,b in liste:
	orbites[b] = a

def nb_orbite(a, orbites):
	if orbites[a] == 'COM':
		return 1
	return 1 + nb_orbite(orbites[a], orbites)

res = 0
for i in orbites:
	if i != "COM":
		res += nb_orbite(i, orbites)

print("Partie 1 :",res)

def ancetres(a, orbites):
	res = []
	while a != "COM":
		res.append(orbites[a])
		a = orbites[a]
	return res

def solve(orbites):
	L1 = ancetres("YOU", orbites)
	L2 = ancetres("SAN", orbites)
	if len(L1) < len(L2):
		L1 = [None]*(len(L2)-len(L1)) + L1
	else:
		L2 = [None]*(len(L1)-len(L2)) + L2
	i = 0
	res = 0
	while L1[i] != L2[i]:
		res += (1 if L1[i] != None else 0)
		res += (1 if L2[i] != None else 0)
		i += 1
	return res

print("Partie 2 :",solve(orbites))