import networkx as nx
import sys
sys.path.append("..")
g = nx.Graph()
node_count = 0
edge_count = 0

node_file = open('../email-Eu-core-department-labels.txt','r')
for line in node_file.readlines():
    line = line.split('\n')[0]
    node = line.split(" ")[0]
    community = line.split(" ")[1]
    g.add_node(node, label=community)
    node_count += 1

node_file.close()

edge_file = open('../email-Eu-core.txt','r')
for line in edge_file.readlines():
    line = line.split('\n')[0]
    node = line.split(" ")[0]
    connecting_node = line.split(" ")[1]
    g.add_edge(node, connecting_node)
    edge_count += 1

print("Nodes: ", node_count, "Edges: ", edge_count)


