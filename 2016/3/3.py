fichier=open('input.txt','r')
texte=fichier.read()
fichier.close()

t=[]
ligne=[]
temp=''
for i in texte:
	if i=='\n':
		ligne.append(int(temp))
		temp=''
		t.append(ligne)
		ligne=[]
	elif i==' ':
		if temp!='':
			ligne.append(int(temp))
			temp=''
	else:
		temp+=i

res=0
for ligne in t:
	if sorted(ligne)[0]+sorted(ligne)[1]>sorted(ligne)[2]:
		res+=1

print(f'Partie 1 : {res}')

#Partie 2

L=[]
for ligne in range(0,len(t),3):
	L.append([t[ligne][0],t[ligne+1][0],t[ligne+2][0]])
	L.append([t[ligne][1],t[ligne+1][1],t[ligne+2][1]])
	L.append([t[ligne][2],t[ligne+1][2],t[ligne+2][2]])

res=0
for ligne in L:
	if sorted(ligne)[0]+sorted(ligne)[1]>sorted(ligne)[2]:
		res+=1

print(f'Partie 2 : {res}')