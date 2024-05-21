with open("input.txt","r") as fichier:
	texte = fichier.read()

# texte = """Step C must be finished before step A can begin.
# Step C must be finished before step F can begin.
# Step A must be finished before step B can begin.
# Step A must be finished before step D can begin.
# Step B must be finished before step E can begin.
# Step D must be finished before step E can begin.
# Step F must be finished before step E can begin."""

t = [[i.split(" ")[1],i.split(" ")[7]] for i in texte.strip().split("\n")]

def conditions(lettre):
	return [a for (a,b) in t if b == lettre]		

def est_disponible(lettre, res):
	for i in conditions(lettre):
		if i not in res:
			return False
	return True

def liste():
	E = set()
	for (a,b) in t:
		E.add(a)
		E.add(b)
	return E

def nettoyage():
	for i in disponible:
		if i in liste_lettre:
			liste_lettre.discard(i)

liste_lettre = liste()
res = ""
disponible = []
compteur = 0

while liste_lettre:
	for lettre in liste_lettre:
			if est_disponible(lettre, res):
				disponible.append(lettre)
	nettoyage()
	if disponible != []:
		disponible.sort()
		res += disponible.pop(0)

print('Partie 1 :',res)

#Partie 2