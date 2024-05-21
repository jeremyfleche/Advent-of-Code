with open('input.txt','r') as fichier:
	texte=fichier.read()

temp=''
t=tuple()
for i in texte:
	if i=='\t' or i=='\n':
		if temp!='':
			t+=(int(temp),)
		temp=''
	else:
		temp+=i

def maximum(t):
	res=0
	maximum=t[0]
	for i in range(1,len(t)):
		if t[i]>maximum:
			maximum=t[i]
			res=i
	return res

def redistribution(t):
	res=[]
	indice=maximum(t)
	x=t[indice]
	t[indice]=0
	for i in range(x):
		indice=(indice+1)%len(t)
		t[indice]+=1


d=dict()
d[t]=[0]
res=0
while True:
	t=list(t)
	redistribution(t)
	res+=1
	t=tuple(t)
	try:
		d[t].append(res)
		break
	except:
		d[t]=[res]

print('Partie 1 :',res)
print('Partie 2 :',d[t][1]-d[t][0])

