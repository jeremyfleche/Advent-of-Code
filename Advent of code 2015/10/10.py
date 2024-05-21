x='1113122113'

def decoupe(s):
	res=[]
	temp=''
	for i in s:
		if temp=='':
			temp+=i
		elif i==temp[len(temp)-1]:
			temp+=i
		else:
			res.append(temp)
			temp=''
			temp+=i
	if temp!='':
		res.append(temp)
	return res

def jeu(x):
	res=''
	for i in decoupe(x):
		res+=str(len(i))+i[0]
	return res

for i in range(40):
	x=jeu(x)

print(f'Partie 1 : {len(x)}')

#Partie 2

x='1113122113'

for i in range(50):
	x=jeu(x)

print(f'Partie 2 : {len(x)}') #Attendre une quinzaine de secondes pour le résultat
