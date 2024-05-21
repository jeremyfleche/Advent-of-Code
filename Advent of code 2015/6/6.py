fichier=open('input.txt','r')
texte=fichier.read()
fichier.close()

t=[]
ligne=''
for i in texte:
	if i=='\n':
		t.append(ligne)
		ligne=''
	else:
		ligne+=i

# turn on = 1
# turn off = 2
# toogle = 3

instructions=[]
for ligne in t:
	instructions.append([])
	if ligne[:7]=='turn on':
		instructions[len(instructions)-1].append(1)
	if ligne[:8]=='turn off':
		instructions[len(instructions)-1].append(2)
	if ligne[:6]=='toggle':
		instructions[len(instructions)-1].append(3)
	nombre=''
	for i in ligne:
		if i.isdigit()==False and nombre!='':
			instructions[len(instructions)-1].append(int(nombre))
			nombre=''
		if i.isdigit():
			nombre+=i
	if nombre!='':
		instructions[len(instructions)-1].append(int(nombre))

grille=[]
for y in range(1000):
	grille.append([])
	for x in range(1000):
		grille[len(grille)-1].append(0)


def turn_on(x1,y1,x2,y2):
	global grille
	for y in range(min(y1,y2),max(y1,y2)+1):
		for x in range(min(x1,x2),max(x1,x2)+1):
			grille[y][x]=1


def turn_off(x1,y1,x2,y2):
	global grille
	for y in range(min(y1,y2),max(y1,y2)+1):
		for x in range(min(x1,x2),max(x1,x2)+1):
			grille[y][x]=0


def toogle(x1,y1,x2,y2):
	global grille
	for y in range(min(y1,y2),max(y1,y2)+1):
		for x in range(min(x1,x2),max(x1,x2)+1):
			grille[y][x]=1-grille[y][x]


for i in instructions:
	if i[0]==1:
		turn_on(i[1],i[2],i[3],i[4])
	if i[0]==2:
		turn_off(i[1],i[2],i[3],i[4])
	if i[0]==3:
		toogle(i[1],i[2],i[3],i[4])


counter=0
for y in grille:
	for x in y:
		if x==1:
			counter+=1

print('Partie 1 : '+str(counter))

#Partie 2

grille=[]
for y in range(1000):
	grille.append([])
	for x in range(1000):
		grille[len(grille)-1].append(0)

def turn_on2(x1,y1,x2,y2):
	global grille
	for y in range(min(y1,y2),max(y1,y2)+1):
		for x in range(min(x1,x2),max(x1,x2)+1):
			grille[y][x]+=1


def turn_off2(x1,y1,x2,y2):
	global grille
	for y in range(min(y1,y2),max(y1,y2)+1):
		for x in range(min(x1,x2),max(x1,x2)+1):
			if grille[y][x]>=1:
				grille[y][x]-=1

def toogle2(x1,y1,x2,y2):
	global grille
	for y in range(min(y1,y2),max(y1,y2)+1):
		for x in range(min(x1,x2),max(x1,x2)+1):
			grille[y][x]+=2


for i in instructions:
	if i[0]==1:
		turn_on2(i[1],i[2],i[3],i[4])
	if i[0]==2:
		turn_off2(i[1],i[2],i[3],i[4])
	if i[0]==3:
		toogle2(i[1],i[2],i[3],i[4])

counter=0
for y in range(len(grille)):
	for x in range(len(grille[y])):
		counter+=grille[y][x]

print('Partie 2 : '+str(counter))