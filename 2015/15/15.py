from math import inf

fichier=open('input.txt','r')
texte=fichier.read()
fichier.close()

print('Attendre une vingtaine de secondes pour le résulat')

temp=''
ligne=[]
t=[]
for i in texte:
	if i=='\n':
		ligne.append(temp)
		temp=''
		t.append(ligne)
		ligne=[]
	elif (i==' ' or i==':' or i==',') and temp!='':
		ligne.append(temp)
		temp=''
	else:
		temp+=i

L=[]
for ligne in t:
	L.append([])
	L[len(L)-1].append(ligne[0])
	for i in range(2,11,2):
		L[len(L)-1].append(int(ligne[i]))

possibilite=[]
for i in range(101):
	for j in range(101):
		for k in range(101):
			for l in range(101):
				if i+j+k+l==100:
					possibilite.append([i,j,k,l])

res=-inf
for i,j,k,l in possibilite:
	t1=i*L[0][1]+j*L[1][1]+k*L[2][1]+l*L[3][1]
	t2=i*L[0][2]+j*L[1][2]+k*L[2][2]+l*L[3][2]
	t3=i*L[0][3]+j*L[1][3]+k*L[2][3]+l*L[3][3]
	t4=i*L[0][4]+j*L[1][4]+k*L[2][4]+l*L[3][4]
	if t1<0 or t2<0 or t3<0 or t4<0:
		if res<0:
			res=0
	elif res<t1*t2*t3*t4:
		res=t1*t2*t3*t4

print(f'Partie 1 : {res}')

# Partie 2
res=-inf
for i,j,k,l in possibilite:
	t1=i*L[0][1]+j*L[1][1]+k*L[2][1]+l*L[3][1]
	t2=i*L[0][2]+j*L[1][2]+k*L[2][2]+l*L[3][2]
	t3=i*L[0][3]+j*L[1][3]+k*L[2][3]+l*L[3][3]
	t4=i*L[0][4]+j*L[1][4]+k*L[2][4]+l*L[3][4]
	t5=i*L[0][5]+j*L[1][5]+k*L[2][5]+l*L[3][5]
	if t1<0 or t2<0 or t3<0 or t4<0 or t5<0:
		if res<0:
			res=0
	elif res<t1*t2*t3*t4 and t5==500:
		res=t1*t2*t3*t4

print(f'Partie 2 : {res}')