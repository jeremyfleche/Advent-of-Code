fichier=open('input.txt','r')
texte=fichier.read()
fichier.close()


t=[]
temp=''
for i in texte:
	if (i==',' or i==' ' or i=='\n') and temp!='':
		t.append(temp)
		temp=''
	elif i!=' ':
		temp+=i

instructions=[]
for i in t:
	instructions.append([])
	instructions[len(instructions)-1].append(i[0])
	instructions[len(instructions)-1].append(int(i[1:]))	

directions=['nord','est','sud','ouest']

facing='nord'

def direction(instruction,x,y):

	global facing
	global directions

	for i in range(len(directions)):
		if facing==directions[i]:
			if instruction[0]=='R':
				facing=directions[(i+1)%len(directions)]
			else:
				facing=directions[(i-1)%len(directions)]
			break

	if facing=='nord':
		return x,y+instruction[1]
	if facing=='est':
		return x+instruction[1],y
	if facing=='sud':
		return x,y-instruction[1]
	if facing=='ouest':
		return x-instruction[1],y

x,y = 0,0

for instruction in instructions:
	x,y=direction(instruction,x,y)

print(f'Partie 1 : {abs(x)+abs(y)}')

# Partie 2

facing='nord'

def direction2(instruction,x,y):

	global facing
	global directions

	for i in range(len(directions)):
		if facing==directions[i]:
			if instruction[0]=='R':
				facing=directions[(i+1)%len(directions)]
			else:
				facing=directions[(i-1)%len(directions)]
			break

endroits=[(0,0)]

x,y = 0,0
running=True
for instruction in instructions:
	if running==False:
		break
	direction2(instruction,x,y)
	for i in range(instruction[1]):
		if facing=='nord':
			y+=1
		if facing=='est':
			x+=1
		if facing=='sud':
			y-=1
		if facing=='ouest':
			x-=1

		if (x,y) not in endroits:
			endroits.append((x,y))
		else:
			running=False
			break
			
print(f'Partie 2 : {abs(x)+abs(y)}')