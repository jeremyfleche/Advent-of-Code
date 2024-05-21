with open('input.txt','r') as f:
	texte=f.read()

t=[]
ligne=[]
for i in texte:
	if i=='\n':
		t.append(ligne)
		ligne=[]
	else:
		ligne.append(int(i))

def visible(t,i,j):
	res=0
	for x in range(i+1,len(t)):
		if t[x][j]>=t[i][j]:
			res+=1
	if res==0:
		return True

	res=0
	for x in range(0,i):
		if t[x][j]>=t[i][j]:
			res+=1
	if res==0:
		return True
	
	res=0
	for x in range(j+1,len(t[0])):
		if t[i][x]>=t[i][j]:
			res+=1
	if res==0:
		return True

	res=0
	for x in range(0,j):
		if t[i][x]>=t[i][j]:
			res+=1
	if res==0:
		return True

	return False

res=0
for i in range(len(t)):
	for j in range(len(t[i])):
		if visible(t,i,j):
			res+=1

print('Partie 1 :',res)

def distance(t,i,j):
	a=0
	for x in range(i+1,len(t)):
		a+=1
		if t[x][j]>=t[i][j]:
			break

	b=0
	for x in range(i-1,-1,-1):
		b+=1
		if t[x][j]>=t[i][j]:
			break
	
	c=0
	for x in range(j+1,len(t[0])):
		c+=1
		if t[i][x]>=t[i][j]:
			break

	d=0
	for x in range(j-1,-1,-1):
		d+=1
		if t[i][x]>=t[i][j]:
			break
	return a*b*c*d


res=0
for i in range(len(t)):
	for j in range(len(t[i])):
		if distance(t,i,j)>res:
			res=distance(t,i,j)

print('Partie 2 :',res)
