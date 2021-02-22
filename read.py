import h5py
import numpy as np


hf = h5py.File('compiere.h5', 'r')
print(hf)
adjacency = hf.get('graph')
print(adjacency)