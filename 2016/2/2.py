fichier=open('input.txt','r')
texte=fichier.read()
fichier.close()

ligne=[]
t=[]
for i in texte:
	if i=='\n':
		t.append(ligne)
		ligne=[]
	else:
		ligne.append(i)

clavier=[
['1','2','3'],
['4','5','6'],
['7','8','9'],
]

def bouton(instruction):
	global i
	global j
	for x in instruction:
		if x=='U':
			if i>0:
				i-=1
		elif x=='D':
			if i<2:
				i+=1
		elif x=='R':
			if j<2:
				j+=1
		else:
			if j>0:
				j-=1

i=1
j=1

res=''
for instruction in t:
	bouton(instruction)
	res+=clavier[i][j]

print(f'Partie 1 : {res}')

# Partie 2

clavier=[
['X','X','1','X','X'],
['X','2','3','4','X'],
['5','6','7','8','9'],
['X','A','B','C','X'],
['X','X','D','X','X']
]


def bouton2(instruction):
	global i
	global j
	for x in instruction:
		new_i=i
		new_j=j
		if x=='U':
			if new_i>0:
				new_i-=1
		if x=='D':
			if new_i<4:
				new_i+=1
		if x=='R':
			if new_j<4:
				new_j+=1
		if x=='L':
			if new_j>0:
				new_j-=1

		if clavier[new_i][new_j]!='X':
			i,j=new_i,new_j

i=2
j=0

res=''
for instruction in t:
	bouton2(instruction)
	res+=clavier[i][j]

print(f'Partie 2 : {res}')