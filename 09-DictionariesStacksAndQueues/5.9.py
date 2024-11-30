import csv

directory = {}

with open("province.csv", "r", encoding="utf-8") as file:
    provinces = csv.DictReader(file)
    with open("vehicle.txt", "r", encoding="utf-8") as file:
        vehicles = file.read()
        list_vehicles = vehicles.splitlines()
        for row in provinces:
            for vehicle in list_vehicles:
                if  vehicle[0] == row["Letter"]:
                    try:
                        directory[f"{row["Name"]}"] += 1
                    except:
                        directory[f"{row["Name"]}"] = 1       

for key,item in directory.items():
    print(f"{key}:{item}")