with open("input.txt") as f:
	texte = f.read().strip()

# texte = "2333133121414131402"

disk = []
d = {}
for i, x in enumerate(texte):
	if i%2==0:
		d[i//2] = (len(disk),int(x))
		disk += [i//2]*int(x)
	else:
		disk += ['.']*int(x)

i = 0
while  i < len(disk) and disk[i] != '.':
	i += 1

for j in range(len(disk)-1, -1, -1):
	if j <= i:
		break
	if disk[j] != '.':
		disk[i] = disk[j]
		disk[j] = '.'
		while  i < len(disk) and disk[i] != '.':
			i += 1

res = 0
i = 0
while disk[i] != '.':
	res += i*disk[i]
	i += 1

print(res)

disk = []
for i, x in enumerate(texte):
	if i%2==0:
		disk += [i//2]*int(x)
	else:
		disk += ['.']*int(x)

def next_space(i):
	while i < len(disk) and disk[i] == '.':
		i += 1
	while i < len(disk) and disk[i] != '.':
		i += 1
	if i >= len(disk):
		return (-1,-1)
	j = 1
	while i+j < len(disk) and disk[i+j] == '.':
		j += 1
	return (i, j)

def next_file(j, deja_traite):
	while 0 <= j and (disk[j] == '.' or disk[j] in deja_traite):
		j -= 1
	if j < 0:
		return -1, -1
	size = 1
	while 0<=j-size and disk[j-size] == disk[j]:
		size += 1
	return j-size+1, size

def first_space():
	return next_space(0)

def first_file(deja_traite):
	return next_file(len(disk)-1, deja_traite)

deja_traite = set()
j, file_size = first_file(deja_traite)

while j != -1:
	i, space_size = first_space()
	while i != -1:
		if i < j and file_size <= space_size:
			for k in range(file_size):
				disk[i+k] = disk[j+k]
				disk[j+k] = '.'
			break
		i, space_size = next_space(i)
	deja_traite.add(disk[j])
	j, file_size = next_file(j, deja_traite)

res = 0
for i in range(len(disk)):
	if disk[i] != '.':
		res += i*disk[i]

# Lancer avec pypy3
print(res)