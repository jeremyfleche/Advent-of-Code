with open("input.txt","r") as fichier:
	texte = fichier.read()

texte = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""

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
	for i in workers:
		if workers[i][0] != "" and workers[i][0] in liste_lettre:
			liste_lettre.discard(workers[i][0])

def travail():
	for i in workers:
		if workers[i][0] != "":
			return True
	return False

def attribution(lettre):
	for i in workers:
		if workers[i][0] == "":
			workers[i] = (lettre, ord(lettre)-64)
			break

def travail_fini():
	res = ""
	for i in workers:
		if workers[i][0] != "" and workers[i][1] == 0:
			res += workers[i][0]
			workers[i] = ("", 0)
	return res

def temps():
	for i in workers:
		lettre, nombre = workers[i]
		workers[i] = ((lettre,nombre-1) if nombre != 0 else (lettre,nombre))

liste_lettre = liste()
nb_workers = 2
workers = {i:("",0) for i in range(nb_workers)}
compteur = 0
res = ""

while liste_lettre or travail():
	res += travail_fini()
	for lettre in liste_lettre:
		if est_disponible(lettre, res):
			attribution(lettre)
	nettoyage()
	temps()
	compteur += 1
	print(workers)

print(compteur-1)