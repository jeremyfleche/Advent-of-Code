texte=open('input.txt','r').read()

def tri(ligne):
	if ligne[0]=='bot':
		return [ligne[1],ligne[5],ligne[6],ligne[10],ligne[11]]
	else:
		return [ligne[1],ligne[5]]

t=[]
ligne=[]
temp=''
for i in texte:
	if i=='\n':
		try:
			temp=int(temp)
		except:
			pass
		ligne.append(temp)
		temp=''
		t.append(tri(ligne))
		ligne=[]
	elif i==' ':
		try:
			temp=int(temp)
		except:
			pass
		ligne.append(temp)
		temp=''
	else:
		temp+=i


def fin(d):
	for i in d:
		if sorted(d[i])==[17,61]:
			return i
	return False

d=dict()


for ligne in t:
	if len(ligne)==5:
		d[ligne[0]]=[]
		if ligne[1]=='bot':
			d[ligne[2]]=[]
		if ligne[3]=='bot':
			d[ligne[4]]=[]

for ligne in t:
	if len(ligne)==2:
		try:
			d[ligne[1]].append(ligne[0])
		except:
			d[ligne[1]]=[ligne[0]]

while True:
	for ligne in t:
		if len(ligne)==5 and len(d[ligne[0]])==2:
			d[ligne[0]]=sorted(d[ligne[0]])
			if ligne[1]=='bot':
				d[ligne[2]].append(min(d[ligne[0]]))
			if ligne[3]=='bot':
				d[ligne[4]].append(max(d[ligne[0]]))
			d[ligne[0]]=[]
		if fin(d)!=False:
			break
	if fin(d)!=False:
		break

print('Partie 1 :',fin(d))

#Partie 2 

output=dict()

for ligne in t:
	if len(ligne)==5:
		d[ligne[0]]=[]
		if ligne[1]=='output':
			output[ligne[2]]=[]
		if ligne[3]=='output':
			output[ligne[4]]=[]
		if ligne[1]=='bot':
			d[ligne[2]]=[]
		if ligne[3]=='bot':
			d[ligne[4]]=[]

for ligne in t:
	if len(ligne)==2:
		try:
			d[ligne[1]].append(ligne[0])
		except:
			d[ligne[1]]=[ligne[0]]



while output[0]==[] or output[1]==[] or output[2]==[]:
	for ligne in t:
		if len(ligne)==5 and len(d[ligne[0]])==2:
			d[ligne[0]]=sorted(d[ligne[0]])
			if ligne[1]=='output':
				output[ligne[2]].append(min(d[ligne[0]]))
			if ligne[3]=='output':
				output[ligne[4]].append(max(d[ligne[0]]))
			if ligne[1]=='bot':
				d[ligne[2]].append(min(d[ligne[0]]))
			if ligne[3]=='bot':
				d[ligne[4]].append(max(d[ligne[0]]))
			d[ligne[0]]=[]

print('Partie 2 :',output[0][0]*output[1][0]*output[2][0])