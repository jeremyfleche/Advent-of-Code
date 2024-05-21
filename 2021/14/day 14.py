

fichier=open('input.txt','r')
texte=fichier.read()
fichier.close


res='CNBPHFBOPCSPKOFNHVKV'
res=[i for i in res]

t=[]
temp=''
ligne=[]

for i in texte:
	if i.isalpha():
		temp+=i
	elif i=='-':
		ligne.append(temp)
		temp=''
	elif i=='\n':
		ligne.append(temp)
		temp=''
		t.append(ligne)
		ligne=[]

for tour in range(10):
	new_res=[i for i in res]
	count=0
	for i in range(len(res)-1):
		for instruction in t:
			if res[i]+res[i+1]==instruction[0]:
				new_res.insert(i+1+count,instruction[1])
				count+=1
	res=[i for i in new_res]
			

d=dict()
for i in res:
	d[i]=0

for i in res:
	d[i]+=1

r=[d[i] for i in d]

print(max(r)-min(r))

# Partie 2


