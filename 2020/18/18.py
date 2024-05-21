with open("input.txt") as f:
	texte = [[j for j in i if j != " "] for i in f.read().strip().splitlines()]

# test = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
# texte = [[j for j in i if j != " "] for i in test.strip().splitlines()]

calculs = []
for i in texte:
	temp = ""
	for j in i:
		temp += j
	calculs.append(temp)

def rabotage(calcul):
	if calcul[0] == "(":
		return calcul[1:-1]
	return calcul

def evaluation(calcul):

	if calcul.isdigit():
		return int(calcul)

	liste = []
	temp = ""
	i = 0
	while i < len(calcul):
		if calcul[i] in "*+":
			if temp != "":
				liste.append(temp)
			temp = ""
			liste.append(calcul[i])
		elif calcul[i] == "(":
			temp = calcul[i]
			parenthese = 1
			while parenthese != 0:
				i += 1
				if calcul[i] == "(":
					parenthese += 1
				if calcul[i] == ")":
					parenthese -= 1
				temp += calcul[i]
			liste.append(temp)
			temp = ""
		else:
			temp += calcul[i]
		i += 1

	if temp != "":
		liste.append(temp)

	res = evaluation(rabotage(liste[0]))
	i = 1
	while i < len(liste):
		if liste[i] == "+":
			res += evaluation(rabotage(liste[i+1]))
		if liste[i] == "*":
			res *= evaluation(rabotage(liste[i+1]))
		i += 2

	return res

print("Partie 1 :",sum([evaluation(calcul) for calcul in calculs]))

def evaluation2(calcul):

	if calcul.isdigit():
		return int(calcul)

	liste = []
	temp = ""
	i = 0
	while i < len(calcul):
		if calcul[i] in "*+":
			if temp != "":
				liste.append(temp)
			temp = ""
			liste.append(calcul[i])
		elif calcul[i] == "(":
			temp = calcul[i]
			parenthese = 1
			while parenthese != 0:
				i += 1
				if calcul[i] == "(":
					parenthese += 1
				if calcul[i] == ")":
					parenthese -= 1
				temp += calcul[i]
			liste.append(temp)
			temp = ""
		else:
			temp += calcul[i]
		i += 1

	if temp != "":
		liste.append(temp)


	i = 1
	while i < len(liste):
		if liste[i] == "+":
			liste[i] = str(evaluation2(rabotage(liste[i-1])) + evaluation2(rabotage(liste[i+1])))
			liste.pop(i+1)
			liste.pop(i-1)
		else:
			i += 1

	res = evaluation2(rabotage(liste[0]))
	i = 1
	while i < len(liste):
		if liste[i] == "*":
			res *= evaluation2(rabotage(liste[i+1]))
		i += 2

	return res

print("Partie 2 :",sum([evaluation2(calcul) for calcul in calculs]))