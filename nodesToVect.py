import sys
import csv

path = sys.argv[1]
output = sys.argv[2]

f = open(path, 'r')
data = f.read().splitlines()
f.close()
print(data)

with open(output, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Class", "FanIn", "FanOut", "If", "Try", "SQL", "McCabe"])
    for d in data:
        d = d.split(';')
        writer.writerow([d[0], d[2], d[4], d[6], d[8], d[10], d[12]])



