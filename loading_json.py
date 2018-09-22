import json

with open('data.json', 'r') as d:
	content = json.load(d)

print(type(content))
print(content)