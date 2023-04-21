import json

# read file
data = None
with open('example.json', 'r') as myfile:
    data = myfile.read()

# parse file
pet_dict = json.loads(data)
# print(data)
ty = pet_dict ['ty']
petkeys = pet_dict.keys()
pass
person_list = list(petkeys)

for person in person_list:
    print(person)
    contents = pet_dict [person]
    print(contents)
pass
