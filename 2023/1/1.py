with open("input.txt") as f:
	texte = f.read().strip()

t = texte.splitlines()

res = 0
for ligne in t:
	nombre = []
	for i in ligne:
		if i.isdigit():
			nombre.append(i)
	res += int(nombre[0]+nombre[-1])

print("Partie 1:",res)

res = 0
d = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, }

for ligne in t:
	nombre = []
	for chiffre in d:
		for i in range(len(ligne)):
			if ligne.find(chiffre,i) != -1:
				nombre.append((d[chiffre],ligne.find(chiffre,i)))
	a = [i for (i,j) in nombre if j == min([i[1] for i in nombre])][0]
	b = [i for (i,j) in nombre if j == max([i[1] for i in nombre])][0]
	res += 10*a+b

print("Partie 2:",res)