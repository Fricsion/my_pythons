import json

data = open('data.json', 'r')
json_dict = json.load( data )

print(json_dict)
