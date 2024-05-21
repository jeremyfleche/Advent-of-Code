with open('input.txt','r') as fichier:
	texte=fichier.read()
	
t=[]
temp=''
for i in texte:
	if i=='\n':
		t.append(int(temp))
		temp=''
	else:
		temp+=i

pointeur=0
res=0
while pointeur<len(t):
	new_pointeur=pointeur+t[pointeur]
	t[pointeur]+=1
	pointeur=new_pointeur
	res+=1

print('Partie 1 :',res)

#Partie 2

t=[]
temp=''
for i in texte:
	if i=='\n':
		t.append(int(temp))
		temp=''
	else:
		temp+=i

pointeur=0
res=0
while pointeur<len(t):
	new_pointeur=pointeur+t[pointeur]
	if t[pointeur]>=3:
		t[pointeur]-=1
	else:
		t[pointeur]+=1
	pointeur=new_pointeur
	res+=1

print('Partie 2 :',res)