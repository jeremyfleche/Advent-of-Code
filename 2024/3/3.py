with open("input.txt") as f:
	texte = f.read().strip()

i = 0
res1 = 0
res2 = 0
a = ""
b = ""
do = True
while i < len(texte):
	if texte[i:i+4] == "do()":
		do = True
		i+=4
	elif texte[i:i+7] == "don't()":
		do = False
		i+=7
	if texte[i:i+4] == "mul(":
		i+=4
		valide = True
		while texte[i].isdigit():
			a += texte[i]
			i += 1
		if texte[i] == ',':
			i+=1
		else:
			valide = False
		while texte[i].isdigit():
			b += texte[i]
			i += 1
		if texte[i] == ')':
			i+=1
		else:
			valide = False
		if valide and a.isdigit() and b.isdigit():
			res1 += int(a)*int(b)
			if do:
				res2 += int(a)*int(b)
		a = ""
		b = ""
	else:
		i+=1

print("Partie 1 :",res1)
print("Partie 2 :",res2)