with open("input.txt") as f:
	texte = f.read().strip()

t = [[j.strip(":,;") for j in i.split(" ")] for i in texte.splitlines()]

def possible(ligne):
	d = {'red':12, 'green':13, 'blue':14}
	for i in range(3,len(ligne),2):
		if int(ligne[i-1]) > d[ligne[i]]:
			return False
	return True

def minimum(ligne):
	d = {'red':0, 'green':0, 'blue':0}
	for i in range(3,len(ligne),2):
		d[ligne[i]] = max(d[ligne[i]],int(ligne[i-1]))
	return d['red']*d['green']*d['blue']

res1 = 0
res2 = 0
for ligne in t:
	if possible(ligne):
		res1 += int(ligne[1])
	res2 += minimum(ligne)

print("Partie 1 :",res1)
print("Partie 2 :",res2)