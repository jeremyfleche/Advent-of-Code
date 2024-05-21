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
	elif i=='[':
		ligne.append(temp)
		temp='['
	elif i==']':
		temp+=i
		ligne.append(temp)
		temp=''
	else:
		temp+=i

def valide(mot):
	for i in range(len(mot)-3):
		if mot[i]==mot[i+3] and mot[i+1]==mot[i+2] and mot[i]!=mot[i+1]:
			return True
	return False

res=0
for ligne in t:
	x=0
	y=0
	for i in range(len(ligne)):
		if ligne[i][0]=='[' and valide(ligne[i])==False:
			x+=1
		if ligne[i][0]!='[' and valide(ligne[i]):
			y+=1
	if x==len(ligne)//2 and y>0:
		res+=1

print(f'Partie 1 : {res}')

# Partie 2

def valide2(mot):
	res=[]
	for i in range(len(mot)-2):
		if mot[i]==mot[i+2] and mot[i]!=mot[i+1]:
			res.append(mot[i:i+3])
	if res==[]:
		return False
	return res

def correspodant(mot):
	return mot[1]+mot[0]+mot[1]

def valide_ligne(ligne):
	for i in ligne:
		if i[0]!='[' and valide2(i)!=False:
			for x in valide2(i):
				for j in ligne:
					if j[0]=='[' and valide2(j)!=False:
						for y in valide2(j):
							if y==correspodant(x):
								return True
	return False

res=0
for ligne in t:
	if valide_ligne(ligne):
		res+=1

print(f'Partie 2 : {res}')