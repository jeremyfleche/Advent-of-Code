with open("input.txt") as f:
	texte = f.read()

t = []
for i in texte.strip().splitlines():
	temp = i.split(" ")
	if temp[0] == "mask":
		t.append(temp[-1])
	else:
		t.append((int(temp[0][4:-1]),int(temp[-1])))

def binaire(decimal):
	res = ""
	x = decimal
	while x != 0:
		res += str(x%2)
		x //= 2
	return '0' * (36 - len(res)) + res[::-1]

def decimal(binaire):
	res = 0
	for i in range(len(binaire)):
		res += int(binaire[i])*2**(len(binaire)-i-1)
	return res

def binaire_mask(nombre,mask):
	res = ""
	x = binaire(nombre)
	for i in range(len(x)):
		res += (x[i] if mask[i] == 'X' else mask[i])
	return res

mem = dict()

for element in t:
	if isinstance(element, str):
		mask = element
	else:
		adress, nombre = element
		mem[adress] = decimal(binaire_mask(nombre,mask))

print("Partie 1 :",sum(mem.values()))

#Partie 2

def adress_mask(adress, mask):
	res = ""
	x = binaire(adress)
	for i in range(len(x)):
		res += (x[i] if mask[i]=="0" else mask[i])
	return res

def liste_adress(adress):
	final_size = 2**adress.count('X')
	res = [adress]
	while len(res) != final_size:
		temp = res.pop(0)
		i = temp.index("X")
		res.append(temp[:i]+'0'+temp[i+1:])
		res.append(temp[:i]+'1'+temp[i+1:])
	return res

mem = dict()

for element in t:
	if isinstance(element, str):
		mask = element
	else:
		adress, nombre = element
		for i in liste_adress(adress_mask(adress,mask)):
			mem[i] = nombre

print("Partie 2 :",sum(mem.values()))