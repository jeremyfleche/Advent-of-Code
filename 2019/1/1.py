fichier=open('input.txt','r')
texte=fichier.read()
fichier.close()

temp=''
t=[]
for i in texte:
	if i=='\n':
		t.append(int(temp))
		temp=''
	else:
		temp+=i

res=0
for i in t:
	res+=i//3-2

print(f'Partie 1 : {res}')

# Partie 2

def carburant(masse):
	x=masse
	res=0
	while x>0:
		if x//3-2 > 0:
			res+=x//3-2
		x=x//3-2
	return res

res=0
for i in t:
	res+=carburant(i)

print(f'Partie 2 : {res}')