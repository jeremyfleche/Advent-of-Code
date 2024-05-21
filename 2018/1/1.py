texte=open('input.txt','r').read()

t=[]
temp=''
for i in texte:
	if i=='\n':
		t.append(int(temp))
		temp=''
	else:
		temp+=i

print('Partie 1 :',sum(t))

def partie2():
	global t
	res=0
	d={0:1}
	while True:
		for i in t:
			res+=i
			try:
				if d[res]==1:
					return res
			except:
				d[res]=1

print('Partie 2 :',partie2())