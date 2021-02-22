import pickle as pkl
import pprint as pp
import random as random
import numpy as np
from scipy import sparse
import pickle as pkl
import csv

clusters = ["Application", "Entity", "Utility"]

names = []
ally = []
allx = []
graph = dict()

inp = open("data/input_compiere.txt", "r")
compiere = inp.read().splitlines()
inp.close()

limit = int((80 * (len(compiere) - 1)) / 100)

# Remove title line
for c in compiere[1:]:
    c = c.split(",")

    # Adding the name to the indexes and deleting from matrix
    names.append(c[0])
    del c[0]
    
    # Adding the class to the ys and deleting from matrix
    label = random.choice(clusters)
    ally.append(label)

    allx.append(c)



npallx = np.asarray(allx, dtype=np.float64)
sparse_allx = sparse.csr_matrix(npallx)


# One hot encoding of all labels

def one_hot(array):
    unique, inverse = np.unique(array, return_inverse=True)
    onehot = np.eye(unique.shape[0])[inverse]
    return onehot

onehot_labels = one_hot(ally)


sparse_tx = sparse_allx[0:limit]
sparse_x = sparse_allx[limit:]

ty = onehot_labels[0:limit]
y = onehot_labels[limit:]




with open('data/compiere_graph.csv', newline='') as cgraph:
    reader = csv.reader(cgraph, delimiter='\t')
    i = 1
    for row in reader:
        if row[0] in names:
            idx = names.index(row[0])
        else: 
            idx = len(names) + i
            i += 1
        if idx not in graph: 
            graph[idx] = []
        if(row[1] in names):
            graph[idx].append(names.index(row[1]))


test_idx = [str(i) for i in range(0, limit)]
print(len(test_idx))
print(sparse_tx.shape)

# Serialize to pickle
with open('data/out/ind.compiere.allx', 'wb') as handle:
    pkl.dump(sparse_allx, handle, protocol=pkl.HIGHEST_PROTOCOL)

with open('data/out/ind.compiere.x', 'wb') as handle:
    pkl.dump(sparse_x, handle, protocol=pkl.HIGHEST_PROTOCOL)

with open('data/out/ind.compiere.tx', 'wb') as handle:
    pkl.dump(sparse_tx, handle, protocol=pkl.HIGHEST_PROTOCOL)

with open('data/out/ind.compiere.ally', 'wb') as handle:
    pkl.dump(onehot_labels, handle, protocol=pkl.HIGHEST_PROTOCOL)

with open('data/out/ind.compiere.y', 'wb') as handle:
    pkl.dump(y, handle, protocol=pkl.HIGHEST_PROTOCOL)

with open('data/out/ind.compiere.ty', 'wb') as handle:
    pkl.dump(ty, handle, protocol=pkl.HIGHEST_PROTOCOL)

with open('data/out/ind.compiere.graph', 'wb') as handle:
    pkl.dump(graph, handle, protocol=pkl.HIGHEST_PROTOCOL)

with open("data/out/ind.compiere.test.index", "w") as handle:
    handle.write("\n".join(test_idx))




