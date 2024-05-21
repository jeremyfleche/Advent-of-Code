with open("input.txt") as f:
	texte = f.read().strip()

texte = "8A004A801A8002F478"

def binaire(hexa):
	d = {'A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
	try:
		return d[hexa]
	except:
		s = ""
		nombre = int(hexa)
		while nombre != 0:
			s += str(nombre%2)
			nombre //= 2
		while len(s) != 4:
			s += "0"

		return s[::-1]

def decimal(binaire):
	res = 0
	for i in range(len(binaire)):
		res += int(binaire[i])*2**(len(binaire)-i-1)
	return res

bits = ""
for i in texte:
	bits += binaire(i)

# bits = "11101110000000001101010000001100100000100011000001100000"

i = len(bits)-1
while bits[i] == "0":
	i -= 1

bits = bits[:i+1]

def longueur(liste):
	return sum(len(i) for i in liste)

def separation(bits):
	bits_type = decimal(bits[3:6])
	liste = []
	while len(bits) >= 11:
		if bits_type == 4:
			t = 6
			while bits[t] != '0':
				t += 5
			liste.append(bits[:t+5])
			bits = bits[t+5:]
		else:
			I = decimal(bits[6])
			if I == 0:
				L = decimal(bits[7:22])
				liste += separation(bits[22:22+L])
				bits = bits[22+L:]
			else:
				L = decimal(bits[7:18])
				liste += separation(bits[18:])
				bits = bits[longueur(separation(bits[18:])):]
	return liste

def algo(bits):
	res = decimal(bits[:3])
	if decimal(bits[3:6]) == 4:
		return res
	for sub_packet in separation(bits):
		res += algo(sub_packet)
	return res

print(algo(bits))