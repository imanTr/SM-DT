import sys
import pandas as pd
import numpy as np
import networkx
import h5py

path = sys.argv[1]
output = sys.argv[2]
# Importing the CSV file sinto a panda dataframe (df)
df = pd.read_csv (path, sep="\t|;", engine="python")

# Extracting edge list ([classA, classB, weight])
edgeList = df.values.tolist()

#Creating an empty graph
G = networkx.DiGraph()

# Looping through edges and adding them to the graph
for i in range(len(edgeList)):
    G.add_edge(edgeList[i][0], edgeList[i][1], weight=edgeList[i][2])

# Generating an adjacency matrix    
# For directed graphs, entry i,j corresponds to an edge from i to j.
A = networkx.adjacency_matrix(G).A

# Converting the graph to numpy matrix for writing
np_graph = networkx.to_numpy_array(G)

# Affiche les noeuds
print(G.nodes)
# Affiche le graph sous forme numpy
print(np_graph)

# Verifie la syntaxe pour importer depuis un np array vers un networkx
# networkx.from_np_array(np_array)

# Writing to h5 binary format
hf = h5py.File(output + '.h5', 'w')
hf.create_dataset('graph', data=np_graph)
hf.create_dataset('adjacency', data=A)
hf.close()


