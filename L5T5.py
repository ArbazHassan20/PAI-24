class Vehicle:
    def __init__(self, make, model, rental_price):
        self.make = make
        self.model = model
        self._rental_price = rental_price  # Encapsulated rental price
        self.available = True

    def check_availability(self):
        return self.available

    def rent_vehicle(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_vehicle(self):
        self.available = True

    def calculate_rental_cost(self, days):
        return self._rental_price * days

    def display_details(self):
        return f"{self.__class__.__name__}: {self.make} {self.model}, Price: ${self._rental_price}/day, Available: {self.available}"


class Car(Vehicle):
    def __init__(self, make, model, rental_price, doors):
        super().__init__(make, model, rental_price)
        self.doors = doors

    def display_details(self):
        return f"{super().display_details()}, Doors: {self.doors}"


class SUV(Vehicle):
    def __init__(self, make, model, rental_price, offroad_capable):
        super().__init__(make, model, rental_price)
        self.offroad_capable = offroad_capable

    def display_details(self):
        return f"{super().display_details()}, Offroad Capable: {self.offroad_capable}"


class Truck(Vehicle):
    def __init__(self, make, model, rental_price, load_capacity):
        super().__init__(make, model, rental_price)
        self.load_capacity = load_capacity

    def display_details(self):
        return f"{super().display_details()}, Load Capacity: {self.load_capacity} tons"


class RentalReservation:
    def __init__(self, customer, vehicle, start_date, end_date):
        self.customer = customer
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date

    def calculate_total_cost(self):
        rental_days = (self.end_date - self.start_date).days
        return self.vehicle.calculate_rental_cost(rental_days)

    def display_details(self):
        return f"Reservation for {self.customer.name}: {self.vehicle.display_details()}, Start: {self.start_date}, End: {self.end_date}, Total Cost: ${self.calculate_total_cost()}"


class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self._contact_info = contact_info  # Encapsulated contact information
        self.rental_history = []

    def rent_vehicle(self, vehicle, start_date, end_date):
        if vehicle.rent_vehicle():
            reservation = RentalReservation(self, vehicle, start_date, end_date)
            self.rental_history.append(reservation)
            return reservation
        return None

    def return_vehicle(self, vehicle):
        vehicle.return_vehicle()

    def display_rental_history(self):
        return "\n".join(reservation.display_details() for reservation in self.rental_history)

class RentalService:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_available_vehicles(self):
        available_vehicles = [vehicle.display_details() for vehicle in self.vehicles if vehicle.check_availability()]
        return "\n".join(available_vehicles) if available_vehicles else "No vehicles available for rent."

# Example usage
rental_service = RentalService()

# Add vehicles
rental_service.add_vehicle(Car("Toyota", "Camry", 40, 4))
rental_service.add_vehicle(SUV("Jeep", "Wrangler", 60, True))
rental_service.add_vehicle(Truck("Ford", "F-150", 50, 2))

# Display available vehicles
available_vehicles = rental_service.display_available_vehicles()
print("Available Vehicles:\n")
print(available_vehicles)
