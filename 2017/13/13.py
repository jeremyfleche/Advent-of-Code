import time
START_TIME = time.time()

with open("input.txt") as f:
    texte = f.read().strip()

# texte = """0: 3
# 1: 2
# 4: 4
# 6: 4"""

layers = {int(line.split(":")[0]):int(line.split(":")[1]) for line in texte.splitlines()}
n = max(layers)

def step(firewall):
    for i in range(n+1):
        if firewall[i] != -1:
            firewall[i][0] += firewall[i][1]
            if firewall[i][0] in (0, layers[i]-1):
                firewall[i][1] = -firewall[i][1]
    return firewall

def part1():
    firewall = [[0, 1] if i in layers else -1 for i in range(n+1)]
    severity = 0
    for i in range(n+1):
        if i in layers:
            if firewall[i][0] == 0:
                severity += i*layers[i]
        firewall = step(firewall)

    return severity

print("Partie 1 :", part1())
print(f"[{int((time.time()-START_TIME)*1000)}ms]")