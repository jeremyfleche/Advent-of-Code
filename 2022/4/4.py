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
	elif i==',' or i=='-':
		ligne.append(int(temp))
		temp=''
	else:
		temp+=i

res=0
for ligne in t:
	if (ligne[0]<=ligne[2] and ligne[1]>=ligne[3]) or (ligne[2]<=ligne[0] and ligne[3]>=ligne[1]):
		res+=1

print('Partie 1 :',res)

def partie2(t):
	res=0
	for ligne in t:
		a=[i for i in range(ligne[0],ligne[1]+1)]
		b=[i for i in range(ligne[2],ligne[3]+1)]
		for i in range(min(ligne[0],ligne[2]),max(ligne[1],ligne[3])+1):
			if i in a and i in b:
				res+=1
				break
	return res

print('Partie 2 :',partie2(t))