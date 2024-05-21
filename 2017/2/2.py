texte=open('input.txt','r').read()

t=[]
ligne=[]
temp=''
for i in texte:
	if i=='\n':
		if temp!='':
			ligne.append(int(temp))
			temp=''
		t.append(ligne)
		ligne=[]
	elif i=='\t':
		if temp!='':
			ligne.append(int(temp))
			temp=''
	else:
		temp+=i

res=0
for ligne in t:
	res+=max(ligne)-min(ligne)

print('Partie 1 :',res)


res=0
for ligne in t:
	for i in ligne:
		for j in ligne:
			if i>j and i/j==i//j:
				res+=i//j

print('Partie 2 :',res)