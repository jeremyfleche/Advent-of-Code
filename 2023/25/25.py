import networkx as nx

with open("input.txt") as f:
	texte = f.read()

# texte = """jqt: rhn xhk nvd
# rsh: frs pzl lsr
# xhk: hfx
# cmg: qnr nvd lhk bvb
# rhn: xhk bvb hfx
# bvb: xhk hfx
# pzl: lsr hfx nvd
# qnr: nvd
# ntq: jqt hfx bvb xhk
# nvd: lhk
# lsr: lhk
# rzs: qnr cmg lsr rsh
# frs: qnr lhk lsr"""

temp = [[j for j in i.split()] for i in texte.strip().splitlines()]

connexions = dict()
for ligne in temp:
	x = ligne[0][:-1]
	E = {i for i in ligne[1:]}
	for i in E:
		if x not in connexions:
			connexions[x] = set()
		if i not in connexions:
			connexions[i] = set()
		connexions[x].add(i)
		connexions[i].add(x)

G = nx.DiGraph()
for i in connexions:
	for j in connexions[i]:
		G.add_edge(i, j, capacity=1.0)
		G.add_edge(j, i, capacity=1.0)

for i in connexions.keys():
	for j in connexions.keys():
		if i!=j:
			cut_value, partition = nx.minimum_cut(G, i, j)
			if cut_value == 3:
				print("Réponse :",len(partition[0])*len(partition[1]))
				exit(0)