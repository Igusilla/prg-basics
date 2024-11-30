import json

with open("09-DictionariesStacksAndQueues/reservations.json", "r", encoding="utf-8") as file:
    data = json.load(file)

def number_of_rooms(data):
    rooms=0
    for room in range(len(data["reservations"])):
        rooms+=1
    
    return rooms

def number_of_paid(file):
    rooms=0
    for room in data["reservations"]:
        if room["paid"]== True:
            rooms+=1
    
    return rooms

def number_of_unpaid(data):
    rooms=0
    for room in data["reservations"]:
        if room["paid"]== False:
            rooms+=1
    
    return rooms

def total_value_of_paid(data):
    value=0
    for room in data["reservations"]:
        if room["paid"]== True:
            value+=room["price_per_night"]*room["nights"]
    
    return value

def total_value_of_unpaid(data):
    value=0
    for room in data["reservations"]:
        if room["paid"]== False:
            value+=room["price_per_night"]*room["nights"]
    
    return value

print("Number of rooms", number_of_rooms(data))
print("Number of paid reservations", number_of_paid(data))
print("Number of unpaid reservations", number_of_unpaid(data))
print("Total value of paid rooms", total_value_of_paid(data))
print("Total value of unpaid rooms", total_value_of_unpaid(data))