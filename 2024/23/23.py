import time
import networkx as nx
START_TIME = time.time()

with open("input.txt") as f:
	texte = f.read().strip()

G = nx.Graph([i.split("-") for i in texte.splitlines()])

cliques = sorted(nx.enumerate_all_cliques(G), key=lambda x: len(x))

print("Partie 1 :", sum(1 for clique in cliques if len(clique)==3 and any(j[0]=='t' for j in clique)))
print("Partie 2 :", ",".join(sorted(cliques[-1])))

print(f"[{int((time.time()-START_TIME)*1000)}ms]")