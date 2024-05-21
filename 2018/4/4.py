with open("input.txt") as f:
	texte = f.read().strip()

planning = []
for ligne in texte.splitlines():
	temp = ligne.split()
	if temp[2][0] == 'G':
		planning.append([])