import json 
import csv

with open('data.json', 'r') as inp:
	data = json.load(inp)

out = csv.writer(open('data.csv', 'w'))

out.writerow(data[0].keys())

for row in data:
	out.writerow(row.values())