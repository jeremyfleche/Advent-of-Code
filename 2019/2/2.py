texte=open('input.txt','r').read()
open('input.txt','r').close()

t=[]
temp=''
for i in texte:
	if i==',':
		t.append(int(temp))
		temp=''
	else:
		temp+=i
t.append(int(temp))

t[1]=12
t[2]=2

def algo(t):
	for i in range(0,len(t),4):
		if t[i]==99:
			break
		if t[i]==1:
			t[t[i+3]]=t[t[i+1]]+t[t[i+2]]
		if t[i]==2:
			t[t[i+3]]=t[t[i+1]]*t[t[i+2]]
	return t[0]

print('Partie 1 :',algo(t))

t=[]
temp=''
for i in texte:
	if i==',':
		t.append(int(temp))
		temp=''
	else:
		temp+=i
t.append(int(temp))

def copie(t):
	res=[]
	for i in t:
		res.append(i)

	return res

res=0
for i in range(100):
	if res!=0:
		break
	for j in range(100):
		liste=copie(t)
		liste[1],liste[2]=i,j
		if algo(liste)==19690720:
			res=100*i+j
			break

print('Partie 2 :',res)
