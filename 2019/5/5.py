with open("input.txt") as f:
	texte = f.read().strip()

# texte = """1002,4,3,4,33"""

liste = [int(i) for i in texte.split(",")]

def extraire(x,i):
	return (x // 10**(i-1)) % 10

def mod(mod_instructions, k, i, t):
	return (t[i+k] if mod_instructions[k-1] == 0 else i+k)

def part1():
	t = [i for i in liste]
	i = 0
	input_value = 1
	while t[i] != 99:
		opcode = t[i]%100
		mod_instructions = [int(i) for i in str(t[i])[::-1][2:]]
		while len(mod_instructions) < 3:
			mod_instructions.append(0)
		if opcode == 1:
			t[mod(mod_instructions, 3, i, t)] = t[mod(mod_instructions, 1, i, t)] + t[mod(mod_instructions, 2, i, t)]
			i += 4
		if opcode == 2:
			t[mod(mod_instructions, 3, i, t)] = t[mod(mod_instructions, 1, i, t)] * t[mod(mod_instructions, 2, i, t)]
			i += 4
		if opcode == 3:
			t[mod(mod_instructions, 3, i, t)] = input_value	
			i += 2
		if opcode == 4:
			input_value = t[mod(mod_instructions, 1, i, t)]
			i += 2
	return input_value

print("Partie 1 :",part1())

# texte = """3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
# 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
# 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"""

liste = [int(i) for i in texte.split(",")]

def part2():
	t = [i for i in liste]
	i = 0
	input_value = 5
	while t[i] != 99:
		opcode = t[i]%100
		mod_instructions = [int(i) for i in str(t[i])[::-1][2:]]
		while len(mod_instructions) < 3:
			mod_instructions.append(0)
		if opcode == 1:
			t[mod(mod_instructions, 3, i, t)] = t[mod(mod_instructions, 1, i, t)] + t[mod(mod_instructions, 2, i, t)]
			i += 4
		if opcode == 2:
			t[mod(mod_instructions, 3, i, t)] = t[mod(mod_instructions, 1, i, t)] * t[mod(mod_instructions, 2, i, t)]
			i += 4
		if opcode == 3:
			t[mod(mod_instructions, 1, i, t)] = input_value	
			i += 2
		if opcode == 4:
			input_value = t[mod(mod_instructions, 1, i, t)]
			i += 2
		if opcode == 5:
			if t[mod(mod_instructions, 1, i, t)] != 0:
				i = t[mod(mod_instructions, 2, i, t)]
			else:
				i += 3
		if opcode == 6:
			if t[mod(mod_instructions, 1, i, t)] == 0:
				i = t[mod(mod_instructions, 2, i, t)]
			else:
				i += 3
		if opcode == 7:
			if t[mod(mod_instructions, 1, i, t)] < t[mod(mod_instructions, 2, i, t)]:
				t[mod(mod_instructions, 3, i, t)] = 1
			else:
				t[mod(mod_instructions, 3, i, t)] = 0
			i += 4
		if opcode == 8:
			if t[mod(mod_instructions, 1, i, t)] == t[mod(mod_instructions, 2, i, t)]:
				t[mod(mod_instructions, 3, i, t)] = 1
			else:
				t[mod(mod_instructions, 3, i, t)] = 0
			i += 4
	return input_value

print("Partie 2 :",part2())