from collections import deque

with open("input.txt") as f:
	texte = f.read().strip()

# texte = """Register A: 2024
# Register B: 0
# Register C: 0

# Program: 0,3,5,4,3,0"""

temp = texte.split("\n\n")
registre = {i+4:int(temp[0].splitlines()[i].split()[-1]) for i in range(3)}
program = list(map(int, temp[1].split()[1].split(',')))

def algo(registre, program, x=None):
	if x != None:
		registre[4] = x
	i = 0
	out = []
	while i < len(program):
		if program[i] == 0:
			registre[4] //= 2**registre.get(program[i+1], program[i+1])
			i += 2
		elif program[i] == 1:
			registre[5] ^= program[i+1]
			i += 2
		elif program[i] == 2:
			registre[5] = registre.get(program[i+1], program[i+1]) % 8
			i += 2
		elif program[i] == 3:
			if registre[4] == 0:
				i += 2
			else:
				i = program[i+1]
		elif program[i] == 4:
			registre[5] ^= registre[6]
			i += 2
		elif program[i] == 5:
			temp = registre.get(program[i+1], program[i+1]) % 8
			out.append(temp)
			i += 2
		elif program[i] == 6:
			registre[5] = registre[4] // 2**registre.get(program[i+1], program[i+1])
			i += 2
		else:
			registre[6] = registre[4] // 2**registre.get(program[i+1], program[i+1])
			i += 2
	return out

res1 = algo(registre, program)
print("Partie 1 :", ','.join([str(i) for i in res1]))

# DFS
def part2(a, n):
	
	# la longueur de l'output généré est la même que celle du programe
	if n > len(program):
		return a

	# Comme on travaille en octal, le a suivant sera 8*a + i
	for i in range(8):
		na = (a << 3) + i
		output = algo(registre, program, na)

		# le bout de longueur n du programme
		target = program[-n:]

		# si l'output correspond au morceau du programme, c'est un candidat
		if output == target:
			x = part2(na, n+1)
			if x != None:
				return x
	return None

res2 = part2(0, 1)
print("Partie 2 :", res2)