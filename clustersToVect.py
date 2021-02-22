import sys
import re

path = sys.argv[1]
output = sys.argv[2]
vect_table = []


f = open(path, 'r')
content = f.read()
f.close()
all_clusters = re.findall(r'\{.*?\}', content) 
matrix = []

nb_clusters = len(all_clusters)
for idx, cluster in enumerate(all_clusters):
    cluster = cluster[1:-1].replace(' ', '')
    cluster = re.split(',|;', cluster)
    for c in cluster:
        l = [c] + [0 for i in range(0, nb_clusters)]
        l[idx + 1] = 1
        matrix.append(l)


with open(output + ".txt", "w") as outfile:
    outfile.write("\n".join(str(item) for item in matrix))


