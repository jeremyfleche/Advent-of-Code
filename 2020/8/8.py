with open('input.txt') as f:
	texte = f.read()

# texte = """nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6"""

instructions = [i.split(" ") for i in texte.strip().split("\n")]

for i in instructions:
	i[1] = int(i[1])

def programme(instruction):
	global accumulator
	if instruction[0] == 'acc':
		accumulator += instruction[1]
		return 1
	elif instruction[0] == "jmp":
		return instruction[1]
	else:
		return 1

def deja_vu(liste,i):
	if i in liste:
		return True
	return False

accumulator = 0
i = 0
liste = []

while not deja_vu(liste,i):
	liste.append(i)
	i += programme(instructions[i])

print("Partie 1 :",accumulator)

# Partie 2


def change(L, x):
	res = [i for i in L]
	if res[x][0] == 'nop':
		res[x] = ['jmp', res[x][1]]
	if res[x][0] == 'jmp':
		res[x] = ['nop', res[x][1]]
	return res

def same(A,B):
	for i in range(len(A)):
		if A[i] != B[i]:
			return False
	return True

for x in range(len(instructions)):
	new_instructions = change(instructions, x)
	accumulator = 0
	i = 0
	liste = []
	while i < len(new_instructions):
		if deja_vu(liste,i):
			break
		liste.append(i)
		temp = i
		i += programme(new_instructions[i])
		if temp+1 == i == len(new_instructions) and not deja_vu(liste,i):
			print("Partie 2 :",accumulator)
			break
