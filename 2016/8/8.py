fichier=open('input.txt','r')
texte=fichier.read()
fichier.close()

t=[]
ligne=[]
temp=''
for i in texte:
	if i=='\n':
		ligne.append(temp)
		temp=''
		t.append(ligne)
		ligne=[]
	elif i==' ':
		ligne.append(temp)
		temp=''
	else:
		temp+=i

for ligne in range(len(t)):
	if t[ligne][0]=='rect':
		L=[]
		L.append(t[ligne][0])
		temp=''
		for i in t[ligne][1]:
			if i.isdigit()==False:
				L.append(int(temp))
				temp=''
			else:
				temp+=i
		L.append(int(temp))
		t[ligne]=L
	elif t[ligne][1]=='row':
		t[ligne]=[t[ligne][1]]+[int(t[ligne][2][2:])]+[int(t[ligne][4])]
	else:
		t[ligne]=[t[ligne][1]]+[int(t[ligne][2][2:])]+[int(t[ligne][4])]

def copie_grille(grille):
	res=[]
	for i in range(len(grille)):
		res.append([])
		for j in range(len(grille[i])):
			res[len(res)-1].append(grille[i][j])
	return res

def affiche(grille):
	for ligne in grille:
		res=''
		for j in ligne:
			res+=j
		print(res)
	print()

def rect(a,b):
	global grille
	for i in range(b):
		for j in range(a):
			grille[i][j]='#'

def rotate_row(y,n):
	global grille
	res=copie_grille(grille)
	for i in range(len(grille)):
		for j in range(len(grille[i])):
			if i==y:
				res[i][j]=grille[i][(j-n)%len(grille[i])]
			else:
				res[i][j]=grille[i][j]
	return res

def rotate_column(x,n):
	global grille
	res=copie_grille(grille)
	for i in range(len(grille)):
		for j in range(len(grille[i])):
			if j==x:
				res[i][j]=grille[(i-n)%len(grille)][j]
			else:
				res[i][j]=grille[i][j]
	return res

grille=[]
for i in range(6):
	grille.append([])
	for j in range(50):
		grille[len(grille)-1].append('.')

for ligne in t:
	if ligne[0]=='rect':
		rect(ligne[1],ligne[2])
	elif ligne[0]=='row':
		grille=rotate_row(ligne[1],ligne[2])
	else:
		grille=rotate_column(ligne[1],ligne[2])

res=0
for i in grille:
	for j in i:
		if j=='#':
			res+=1

print(f'Partie 1 : {res}',end='\n\n')

affiche(grille)

print(f'Partie 2 : CFLELOYFCS')  