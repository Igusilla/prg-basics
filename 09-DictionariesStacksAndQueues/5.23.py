import json

with open("euro.json", "r") as file:
    data = json.load(file)
    print("         Data              Buying Rate              Selling Rate         ")
    for rate in data["rates"]:
        print(f"       {rate["effectiveDate"]}              {rate["bid"]}                {rate["ask"]}         ")