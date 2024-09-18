class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def calculate_fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def calculate_fare(self):
        base_fare = super().calculate_fare()
        maintenance_charge = base_fare * 0.10
        total_fare = base_fare + maintenance_charge
        return total_fare

# Create an instance of Vehicle
car = Vehicle(seating_capacity=5)
print(f"Car fare: ${car.calculate_fare()}")

# Create an instance of Bus
bus = Bus(seating_capacity=30)
print(f"Bus fare: ${bus.calculate_fare()}")
