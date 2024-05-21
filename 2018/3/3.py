with open('input.txt','r') as fichier:
	texte=fichier.read()

t=[]
ligne=[]
temp=''
for i in texte:
	if i=='\n':
		ligne.append(int(temp))
		temp=''
		t.append(ligne)
		ligne=[]
	elif i.isdigit()==False:
		if temp!='':
			ligne.append(int(temp))
		temp=''
	else:
		temp+=i

def dimensions(t):
	max_x=0
	max_y=0
	for ligne in t:
		if ligne[1]+ligne[3]>max_x:
			max_x=ligne[1]+ligne[3]
		if ligne[2]+ligne[4]>max_y:
			max_y=ligne[2]+ligne[4]
	return max_x,max_y

def grille(x,y):
	res=[]
	for i in range(y):
		res.append([])
		for j in range(x):
			res[len(res)-1].append(0)
	return res

def change(grille,x,y,n):
	if grille[y][x]==0:
		grille[y][x]=n
	else:
		grille[y][x]='X'

max_x,max_y=dimensions(t)
grille=grille(max_x,max_y)

for ligne in t:
	for y in range(ligne[2],ligne[2]+ligne[4]):
		for x in range(ligne[1],ligne[1]+ligne[3]):
			change(grille,x,y,ligne[0])

res=0
for i in grille:
	for j in i:
		if j=='X':
			res+=1

print('Partie 1 :',res)

def partie2(t,grille):
	for ligne in t:
		if sum([i.count(ligne[0]) for i in grille])==ligne[3]*ligne[4]:
			return ligne[0]

print('Partie 1 :',partie2(t,grille))