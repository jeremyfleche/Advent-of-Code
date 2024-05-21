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

def changement_etat(i,j):
	global t
	res=0
	if i==0:
		if j==0:
			if t[i][j+1]=='#':
				res+=1
			if t[i+1][j]=='#':
				res+=1
			if t[i+1][j+1]=='#':
				res+=1
		elif j==len(t[i])-1:
			if t[i][j-1]=='#':
				res+=1
			if t[i+1][j-1]=='#':
				res+=1
			if t[i+1][j]=='#':
				res+=1
		else:
			if t[i][j-1]=='#':
				res+=1
			if t[i+1][j-1]=='#':
				res+=1
			if t[i+1][j]=='#':
				res+=1
			if t[i+1][j+1]=='#':
				res+=1
			if t[i][j+1]=='#':
				res+=1
	elif i==len(t)-1:
		if j==0:
			if t[i-1][j]=='#':
				res+=1
			if t[i-1][j+1]=='#':
				res+=1
			if t[i][j+1]=='#':
				res+=1
		elif j==len(t[i])-1:
			if t[i][j-1]=='#':
				res+=1
			if t[i-1][j-1]=='#':
				res+=1
			if t[i-1][j]=='#':
				res+=1
		else:
			if t[i][j-1]=='#':
				res+=1
			if t[i-1][j-1]=='#':
				res+=1
			if t[i-1][j]=='#':
				res+=1
			if t[i-1][j+1]=='#':
				res+=1
			if t[i][j+1]=='#':
				res+=1
	else:
		if j==0:
			if t[i-1][j]=='#':
				res+=1
			if t[i-1][j+1]=='#':
				res+=1
			if t[i][j+1]=='#':
				res+=1
			if t[i+1][j+1]=='#':
				res+=1
			if t[i+1][j]=='#':
				res+=1
		elif j==len(t[i])-1:
			if t[i-1][j]=='#':
				res+=1
			if t[i-1][j-1]=='#':
				res+=1
			if t[i][j-1]=='#':
				res+=1
			if t[i+1][j-1]=='#':
				res+=1
			if t[i+1][j]=='#':
				res+=1
		else:
			if t[i-1][j-1]=='#':
				res+=1
			if t[i-1][j]=='#':
				res+=1
			if t[i-1][j+1]=='#':
				res+=1
			if t[i][j-1]=='#':
				res+=1
			if t[i][j+1]=='#':
				res+=1
			if t[i+1][j-1]=='#':
				res+=1
			if t[i+1][j]=='#':
				res+=1
			if t[i+1][j+1]=='#':
				res+=1

	if t[i][j]=='#':
		if res==2 or res==3:
			return '#'
		else:
			return '.'

	if t[i][j]=='.':
		if res==3:
			return '#'
		else:
			return '.'

def etape(t):
	L=[]
	for i in range(len(t)):
		L.append([])
		for j in range(len(t[i])):
			L[len(L)-1].append(changement_etat(i,j))
	return L

for j in range(100):
	t=etape(t)

res=0
for i in t:
	for j in i:
		if j=='#':
			res+=1

print(f'Partie 1 : {res}')

#Partie 2

ligne=[]
t=[]
for i in texte:
	if i=='\n':
		t.append(ligne)
		ligne=[]
	else:
		ligne.append(i)

def changement_etat2(i,j):
	global t
	res=0
	if i==0:
		if j==0 or j==len(t[i])-1:
			return '#'
		else:
			if t[i][j-1]=='#':
				res+=1
			if t[i+1][j-1]=='#':
				res+=1
			if t[i+1][j]=='#':
				res+=1
			if t[i+1][j+1]=='#':
				res+=1
			if t[i][j+1]=='#':
				res+=1
	elif i==len(t)-1:
		if j==0 or j==len(t[i])-1:
			return '#'
		else:
			if t[i][j-1]=='#':
				res+=1
			if t[i-1][j-1]=='#':
				res+=1
			if t[i-1][j]=='#':
				res+=1
			if t[i-1][j+1]=='#':
				res+=1
			if t[i][j+1]=='#':
				res+=1
	else:
		if j==0:
			if t[i-1][j]=='#':
				res+=1
			if t[i-1][j+1]=='#':
				res+=1
			if t[i][j+1]=='#':
				res+=1
			if t[i+1][j+1]=='#':
				res+=1
			if t[i+1][j]=='#':
				res+=1
		elif j==len(t[i])-1:
			if t[i-1][j]=='#':
				res+=1
			if t[i-1][j-1]=='#':
				res+=1
			if t[i][j-1]=='#':
				res+=1
			if t[i+1][j-1]=='#':
				res+=1
			if t[i+1][j]=='#':
				res+=1
		else:
			if t[i-1][j-1]=='#':
				res+=1
			if t[i-1][j]=='#':
				res+=1
			if t[i-1][j+1]=='#':
				res+=1
			if t[i][j-1]=='#':
				res+=1
			if t[i][j+1]=='#':
				res+=1
			if t[i+1][j-1]=='#':
				res+=1
			if t[i+1][j]=='#':
				res+=1
			if t[i+1][j+1]=='#':
				res+=1

	if t[i][j]=='#':
		if res==2 or res==3:
			return '#'
		else:
			return '.'

	if t[i][j]=='.':
		if res==3:
			return '#'
		else:
			return '.'

def etape2(t):
	L=[]
	for i in range(len(t)):
		L.append([])
		for j in range(len(t[i])):
			L[len(L)-1].append(changement_etat2(i,j))
	return L

for j in range(100):
	t=etape2(t)

res=0
for i in t:
	for j in i:
		if j=='#':
			res+=1

print(f'Partie 2 : {res}')