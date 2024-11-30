import json

with open("dogs.json", 'r', encoding='utf-8') as file:
    data = json.load(file)

for dog in data:
    if dog["age"]<5:
        for key, item in dog.items():
            print(f"{key}:{item}")
        print()