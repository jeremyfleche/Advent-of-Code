with open("input.txt") as f:
	texte = f.read()

# texte = """class: 0-1 or 4-19
# row: 0-5 or 8-19
# seat: 0-13 or 16-19

# your ticket:
# 11,12,13

# nearby tickets:
# 3,9,18
# 15,1,5
# 5,14,9"""

temp = texte.strip().split("\n\n")

temp_field1 = temp[0].splitlines()
fields = [[int(j) for j in i.split(" ")[-3].split("-")+i.split(" ")[-1].split("-")] for i in temp_field1]
my_ticket = [int(i) for i in temp[1].splitlines()[1].split(",")]
tickets = [[int(j) for j in i.split(",")] for i in temp[2].splitlines()[1:]]

def in_field(value,fields):
	for field in fields:
		if field[0] <= value <= field[1] or field[2] <= value <= field[3]:
			return True
	return False

def valide(ticket,fields):
	res = []
	for value in ticket:
		if not in_field(value, fields):
			res.append(value)
	return res

res = 0
for ticket in tickets:
	res += sum(valide(ticket,fields))

print("Partie 1 :",res)

#Partie 2

def which_field(field):
	global my_ticket
	global tickets
	global fields
	liste = tickets + [my_ticket]
	liste_valide = [i for i in liste if valide(i,fields) == []]
	res = set([i for i in range(len(my_ticket))])
	for ticket in liste_valide:
		for i in range(len(ticket)):
			if field[0] <= ticket[i] <= field[1] or field[2] <= ticket[i] <= field[3]:
				pass
			else:
				res.remove(i)
	return res

d = dict()
liste = []
for field in fields:
	liste.append(which_field(field))

deja_pris = set()
while len(d) != len(fields):
	for i in range(len(liste)):
		if len(liste[i] - deja_pris) == 1:
			d[i] = list(liste[i] - deja_pris)[0]
			deja_pris.add(list(liste[i] - deja_pris)[0])

res = 1
for i in range(6):
	res *= my_ticket[d[i]]

print("Partie 2 :",res)
