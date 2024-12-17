class Phone():
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color
    
    def TurnOn(self):
        print("Turning On")

    def TurnOff(self):
        print("Turning Off")

    def ChangingMode(self):
        print("Changing mode to battery saving")
    
    def PrintSpecifications(self):
        print(f"Brand: {self.brand}. Year: {self.year}. Color: {self.color}")

def main():
    smarphone = Phone("Samsung", 2024, "red")
    smarphone.TurnOn()
    smarphone.TurnOff()
    smarphone.ChangingMode()
    smarphone.PrintSpecifications()
    
if __name__=="__main__":
    main()