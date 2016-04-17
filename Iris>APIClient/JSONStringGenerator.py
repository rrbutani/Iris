import json

array = []

for i in range(0, 179):
	array.append(0xFF00FF)
print array

#return

print json.dumps(array)

print json.loads(json.dumps(array))

print json.loads(json.dumps(array))[3]
