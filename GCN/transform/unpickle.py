import pickle as pkl
import pprint as pp

with open("../gcn/data/ind.citeseer.allx", 'rb') as f:
    allx = pkl.load(f, encoding='latin1')

with open("../gcn/data/ind.citeseer.x", 'rb') as f:
    x = pkl.load(f, encoding='latin1')

with open("../gcn/data/ind.citeseer.tx", 'rb') as f:
    tx = pkl.load(f, encoding='latin1')

with open("../gcn/data/ind.citeseer.ally", 'rb') as f:
    ally = pkl.load(f, encoding='latin1')

print(allx)