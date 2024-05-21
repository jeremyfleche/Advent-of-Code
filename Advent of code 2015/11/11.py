x='vzbxkghb'

alphabet='abcdefghijklmnopqrstuvwxyz'



def incrementation(s):
	x=[i for i in s]
	x=[x[i] for i in range(len(x)-1,-1,-1)]
	x[0]=chr((ord(x[0])-97+1)%26+97)
	i=0
	while True:
		if x[i]=='a':
			i+=1
			x[i]=chr((ord(x[i])-97+1)%26+97)
		else:
			break

	return [x[i] for i in range(len(x)-1,-1,-1)]	



def suite(s):
	global alphabet
	for i in range(2,len(s)):
		if s[i-2]+s[i-1]+s[i] in alphabet:
			return True
	return False

def deux_paire(s):
	deja_pris=[]
	for i in range(len(s)-1):
		if s[i]==s[i+1] and i not in deja_pris:
			deja_pris.append(i+1)
	return len(deja_pris)>1

def lettres_valides(s):
	return 'i' not in s and 'o' not in s and 'l' not in s

def valide(s):
	if suite(s) and deux_paire(s) and lettres_valides(s):
		return True
	return False




while valide(x)==False:
	x=(incrementation(x))

res=''
for i in x:
	res+=i

print(f'Partie 1 : {res}')

x=incrementation(res)

while valide(x)==False:
	x=(incrementation(x))

res=''
for i in x:
	res+=i

print(f'Partie 2 : {res}')