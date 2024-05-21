from math import inf,lcm

with open("input.txt") as f:
	texte = f.read()

# texte = """939
# 7,13,x,x,59,x,31,19"""

current_time = int(texte.strip().split("\n")[0])
bus = [int(i) for i in texte.strip().split("\n")[1].split(",") if i != "x"]

def temps_restant(bus):
	global current_time
	return (current_time // bus * bus + bus) - current_time

minimum = inf
minimum_id = "?"

for i in bus:
	if temps_restant(i) < minimum:
		minimum = temps_restant(i)
		minimum_id = i

print("Partie 1 :",minimum*minimum_id)

# Partie 2

temp = texte.strip().split("\n")[1].split(",")
bus = [(int(temp[i]),i) for i in range(len(temp)) if temp[i] != 'x']

def solve(liste):
	res = 0
	n = 1
	for bus, decalage in liste:
		while (res + decalage) % bus != 0:		# Tant que res + le décalage n'est pas un multiple de bus
			res += n 							# On ajoute à res le ppcm des bus que l'on avait avant
		n = lcm(n, bus)			# A chaque fois on recalcule le ppcm des bus déjà traités pour monter plus vite vers la réponse (sinon on monterait de 1 par 1 et cela serait trop long)
	return res

print("Partie 2 :",solve(bus))