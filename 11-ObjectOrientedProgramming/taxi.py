class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
        return self.fare
    
    def print_receipt(self):
        print(f'Distance: {self.distance}km, Rate per km: {self.rate_per_km}, Fare: {self.calculate_fare(self.distance)}')

def main():
    # your program
    ride1 = TaxiRide(2)
    ride1.distance = 100
    ride1.print_receipt()

    ride2 = TaxiRide(1.5)
    ride2.distance = 30
    ride2.print_receipt()


if __name__ == "__main__":
    main()
