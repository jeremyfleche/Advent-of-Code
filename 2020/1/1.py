texte=open('input.txt','r').read()

t=[]
temp=''
for i in texte:
	if i=='\n':
		t.append(int(temp))
		temp=''
	else:
		temp+=i

def partie1(t):
	for i in t:
		for j in t:
			if i+j==2020:
				return i*j

print('Partie 1 :',partie1(t))

#Partie 2

def partie2(t):
	for i in t:
		for j in t:
			for k in t:
				if i+j+k==2020:
					return i*j*k

print('Partie 2 :',partie2(t))