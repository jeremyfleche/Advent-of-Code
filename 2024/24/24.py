import time
from collections import deque
from functools import cache
START_TIME = time.time()

with open("input.txt") as f:
	texte = f.read().strip()

# texte = """x00: 0
# x01: 1
# x02: 0
# x03: 1
# x04: 0
# x05: 1
# y00: 0
# y01: 0
# y02: 1
# y03: 1
# y04: 0
# y05: 1

# x00 AND y00 -> z05
# x01 AND y01 -> z02
# x02 AND y02 -> z01
# x03 AND y03 -> z03
# x04 AND y04 -> z04
# x05 AND y05 -> z00"""

temp = texte.split("\n\n")
bits = {}
for line in temp[0].splitlines():
	a,b = line.split(": ")
	bits[a] = int(b)

x = 0
y = 0
for i in sorted(bits, reverse=True):
	if i.startswith('x'):
		x = 2*x + bits[i]
	else:
		y = 2*y + bits[i]

ops = {}
max_z = 0
for line in temp[1].splitlines():
	a,op,b,_,c = line.split()
	ops[c] = (a,op,b)
	if c.startswith('z'):
		max_z = max(max_z, int(c[1:]))

def compute(bit):
	if bit in bits:
		return bits[bit]
	a,op,b = ops[bit]
	if op == 'OR':
		bits[bit] = compute(a) | compute(b)
	elif op == 'AND':
		bits[bit] = compute(a) & compute(b)
	else:
		bits[bit] = compute(a) ^ compute(b)
	return bits[bit]

def part1():
	for i in range(max_z+1):
		bit = 'z' + str(i).zfill(2)
		compute(bit)
	res = 0
	for i in range(max_z,-1,-1):
		bit = 'z' + str(i).zfill(2)
		res = (res << 1) | bits[bit]
	return res

def tree(bit, d=0, space='\t'):
	if bit not in ops:
		return space*d + bit + "\n"
	a,op,b = ops[bit]
	return space*d  + f"{bit} {op}\n" + tree(a, d+1, space) + tree(b, d+1, space)

def sum_valid(wire, num):
	if wire not in ops:
		return False
	a,op,b = ops[wire]
	if op != "XOR":
		return False
	return {a,b} == {f"x{num:02}", f"y{num:02}"}

def carry1_valid(wire, num):
	if wire not in ops:
		return False
	a,op,b = ops[wire]
	if op != "AND":
		return False
	return {a,b} == {f"x{num:02}", f"y{num:02}"}

def carry2_valid(wire, num):
	if wire not in ops:
		return False
	a,op,b = ops[wire]
	if op != "AND":
		return False
	return sum_valid(a, num) and carry_valid(b, num) or sum_valid(b, num) and carry_valid(a, num)

def carry_valid(wire, num):
	if wire not in ops:
		return False
	a,op,b = ops[wire]
	if num == 1:
		if op == "AND":
			return {a,b} == {"x00", "y00"}
	if op != "OR":
		return False
	return carry1_valid(a, num-1) and carry2_valid(b, num-1) or carry1_valid(b, num-1) and carry2_valid(a, num-1)

def is_valid(wire, num):
	if wire not in ops:
		return False
	a,op,b = ops[wire]
	if op != "XOR":
		return False
	if num == 0:
		return {a,b} == {"x00", "y00"}
	return sum_valid(a, num) and carry_valid(b, num) or sum_valid(b, num) and carry_valid(a, num)

def nb_valid(ops):
	num = 0
	wire = f"z{num:02}"
	res = 0
	while wire in ops:
		if is_valid(wire, num):
			res += 1
		num += 1
		wire = f"z{num:02}"
	return res

def part2():
	res = []
	for _ in range(4):
		current_nb_valid = nb_valid(ops)
		for a in ops:
			for b in ops:
				if a == b:
					continue
				ops[a], ops[b] = ops[b], ops[a]
				new_nb_valid = nb_valid(ops)
				if new_nb_valid > current_nb_valid:
					current_nb_valid = new_nb_valid
					res += [a,b]
					break
				ops[a], ops[b] = ops[b], ops[a]
			else:
				continue
			break
	return ','.join(sorted(res))

print("Partie 1 :", part1())

# attendre environ 30s avec pypy3
print("Partie 2 :",part2())

print(f"[{int((time.time()-START_TIME)*1000)}ms]")