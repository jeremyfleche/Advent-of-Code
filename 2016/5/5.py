import hashlib

def MD5(mot):
	return hashlib.md5(mot.encode('utf-8')).hexdigest()

res=''
x=0
while len(res)!=8:
	if MD5('reyedfim'+str(x))[:5]=='00000':
		res+=MD5('reyedfim'+str(x))[5]
	x+=1

print(f'Partie 1 : {res}') # attendre 25 secondes environ pour le résultat

#Partie 2

res=['?','?','?','?','?','?','?','?']
x=0
while True:
	if MD5('reyedfim'+str(x))[:5]=='00000' and MD5('reyedfim'+str(x))[5].isdigit() and int(MD5('reyedfim'+str(x))[5])<len(res):
		if res[int(MD5('reyedfim'+str(x))[5])]=='?':
			res[int(MD5('reyedfim'+str(x))[5])]=MD5('reyedfim'+str(x))[6]
	if '?' not in res:
		break
	x+=1

s=''
for i in res:
	s+=i

print(f'Partie 2 : {s}') # attendre 110 secondes pour avoir le deuxième résultat