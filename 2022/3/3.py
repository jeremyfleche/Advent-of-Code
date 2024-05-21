texte=open('input.txt','r').read()

t=[]
ligne=[]
temp=''
for i in texte:
	if i=='\n':
		ligne.append(temp[:len(temp)//2])
		ligne.append(temp[len(temp)//2:])
		temp=''
		t.append(ligne)
		ligne=[]
	else:
		temp+=i

def valide(ligne):
	for i in ligne[0]:
		for j in ligne[1]:
			if i==j:
				if i.isupper():
					return ord(i)-38
				return ord(i)-96


res=0
for ligne in t:
	res+=valide(ligne)

print('Partie 1 :',res)

t=[]
temp=''
for i in texte:
	if i=='\n':
		t.append(temp)
		temp=''
	else:
		temp+=i

liste=[]
for i in range(0,len(t),3):
	liste.append(t[i:i+3])

def valide2(ligne):
	for i in ligne[0]:
		for j in ligne[1]:
			for k in ligne[2]:
				if i==j==k:
					if i.isupper():
						return ord(i)-38
					return ord(i)-96

res=0
for ligne in liste:
	res+=valide2(ligne)

print('Partie 2 :',res)