import json

with open('filess-page-2-table-2.json', 'r') as json_file:
    json_object = json.load(json_file)

print(json_object)

print(json.dumps(json_object))

print(json.dumps(json_object, indent=1))