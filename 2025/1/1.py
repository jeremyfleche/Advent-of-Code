import time
START_TIME = time.time()

with open("input.txt") as f:
    texte = f.read().strip()

lines = texte.splitlines()

dial = 50
res1 = 0
res2 = 0

for line in lines:
    value = int(line[1:])
    if line[0] == 'L':
        res2 += abs((dial - value) // 100)
        dial = (dial - value) % 100
    else:
        res2 += (dial + value) // 100
        dial = (dial + value) % 100

    if dial == 0:
        res1 += 1

print("Partie 1:", res1)
print("Partie 2:", res2)

print(f"[{int((time.time()-START_TIME)*1000)}ms]")
