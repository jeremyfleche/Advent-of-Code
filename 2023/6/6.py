with open("input.txt") as f:
	texte = f.read()

t = [[int(i) for i in ligne.split()[1:]] for ligne in texte.splitlines()]

# On peut résoudre le problème en parcourant toutes les valeurs possibles et en regardant lesquelles marchent
# Mais il y a plus rapide
# On veut x(duree-x) > 0 donc -x² + x*duree - record > 0     -->	équation très simple
# Cette fonction prend en paramètre la durée et le record et renvoie le nombre de valeurs de x qui rendent vraies cette inégalité
def f(duree, record):
	delta = duree**2 - 4*record
	x1 = (-duree-delta**(1/2))/-2
	x2 = (-duree+delta**(1/2))/-2
	return abs(int(x1)-int(x2))

res = 1
for i in range(len(t[0])):
	duree = t[0][i]
	record = t[1][i]
	res *= f(duree,record)

print("Partie 1 :",res)

# Partie 2

record = ""
duree = ""
t = texte.splitlines()
for i in range(len(t[0])):
	duree += t[0][i] if t[0][i].isdigit() else ""
	record += t[1][i] if t[1][i].isdigit() else ""
record = int(record)
duree = int(duree)

print("Partie 2 :", f(duree,record))