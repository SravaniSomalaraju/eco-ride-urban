class Vehicle:
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = battery_percentage

        self.__maintenance_status = "Available"         #uc1
        self.__rental_price = 0.0

    def set_battery_percentage(self, battery):
        if battery >= 0 and battery <= 100:
            self.battery_percentage = battery
        else:
            print("Battery percentage must be between 0 and 100")

    def get_battery_percentage(self):
        return self.battery_percentage
    
    def set_maintenance_status(self, status):
        self.__maintenance_status = status

    def get_maintenance_status(self):
        return self.__maintenance_status

    def set_rental_price(self, price):
        if price >= 0:
            self.__rental_price = price
        else:
            print("Rental price cannot be negative")

    def get_rental_price(self):
        return self.__rental_price
    

class ElectricCar(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage)
        self.seating_capacity = seating_capacity


class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speed_limit = max_speed_limit
