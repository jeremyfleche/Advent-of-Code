with open("input.txt") as f:
	texte = f.read()

# texte = """LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)"""


t = texte.split("\n\n")[0]

instructions = [[ligne[:3], (ligne[7:10],ligne[12:15])] for ligne in texte.split("\n\n")[1].splitlines()]
d = dict()
for ligne in instructions:
	d[ligne[0]] = ligne[1]

current = 'AAA'
step = 0
i = 0
while current != "ZZZ":
	if t[step%len(t)] == "L":
		current = d[current][0]
	else:
		current = d[current][1]
	step += 1

print("Partie 1 :",step)

def pgcd(a,b):
	if a%b == 0:
		return b
	else:
		return pgcd(b, a%b)

def ppcm(a,b):
	return a*b//pgcd(a,b)

def ppcm_liste(liste):
	if len(liste) == 0:
		return 0
	if len(liste) == 1:
		return liste[0]
	res = ppcm(liste[0],liste[1])
	for i in range(2,len(liste)):
		res = ppcm(res, liste[i])
	return res

debut = [i for i in d if i[2]=="A"]
fin = [i for i in d if i[2]=="Z"]
liste = []
for element in debut:
	current = element
	step = 0
	i = 0
	while current not in fin:
		if t[step%len(t)] == "L":
			current = d[current][0]
		else:	
			current = d[current][1]
		step += 1
	liste.append(step)

print("Partie 2 :",ppcm_liste(liste))