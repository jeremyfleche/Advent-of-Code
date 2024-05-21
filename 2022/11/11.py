with open('input.txt','r') as f:
	texte=f.read()

t=[[j.strip() for j in i.split('\n') if j!=''] for i in texte.split('\n\n')]

for ligne in range(len(t)):
	t[ligne][0] = t[ligne][0][len(t[ligne][0])-2]
	t[ligne][1] = [int(i) for i in t[ligne][1][16:].split(',')]
	t[ligne][2] = t[ligne][2][11:].split()
	t[ligne][3] = int(t[ligne][3][19:])
	t[ligne][4] = int(t[ligne][4][len(t[ligne][4])-1])
	t[ligne][5] = int(t[ligne][5][len(t[ligne][5])-1])

d = dict()
count = dict()
for ligne in t:
	count[ligne[0]] = 0
	for item in ligne[1]:
		try:
			d[ligne[0][0]].append(item)
		except:
			d[ligne[0][0]] = [item]

for _ in range(20):
	for ligne in t:
		count[ligne[0]]+=len(d[ligne[0]])
		for item in d[ligne[0]]:
			worry_level = item
			if ligne[2][4].isdigit():
				if ligne[2][3] == '*':
					worry_level *= int(ligne[2][4])
				else:
					worry_level += int(ligne[2][4])
			if ligne[2][4].isdigit() == False:
				if ligne[2][3] == '*':
					worry_level *= worry_level
				else:
					worry_level += worry_level
			worry_level = worry_level//3
			if worry_level%ligne[3]==0:
				d[str(ligne[4])].append(worry_level)
			else:
				d[str(ligne[5])].append(worry_level)

		d[ligne[0]] = []

temp = sorted([i for i in count.values()])
print('Partie 1 :',temp[-2]*temp[-1])

# Partie 2

d = dict()
count = dict()
for ligne in t:
	count[ligne[0]] = 0
	for item in ligne[1]:
		try:
			d[ligne[0][0]].append(item)
		except:
			d[ligne[0][0]] = [item]

lcm = 1
for ligne in t:
	lcm *= ligne[3]
for i in range(10000):
	for ligne in t:
		count[ligne[0]]+=len(d[ligne[0]])
		for item in d[ligne[0]]:
			worry_level = item
			worry_level %= lcm
			if ligne[2][4].isdigit():
				if ligne[2][3] == '*':
					worry_level *= int(ligne[2][4])
				else:
					worry_level += int(ligne[2][4])
			if ligne[2][4].isdigit() == False:
				if ligne[2][3] == '*':
					worry_level *= worry_level
				else:
					worry_level += worry_level
			if worry_level%ligne[3]==0:
				d[str(ligne[4])].append(worry_level)
			else:
				d[str(ligne[5])].append(worry_level)
		d[ligne[0]] = []

temp = sorted([i for i in count.values()])
print('Partie 2 :',temp[len(temp)-2]*temp[len(temp)-1])
