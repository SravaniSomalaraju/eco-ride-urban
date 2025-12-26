import json
import csv
import os
from vehicle import ElectricCar, ElectricScooter
class FleetManager:
    def __init__(self):
        # Dictionary: Hub Name -> List of Vehicles
        self.hubs = {}

    #uc6: add hub_name
    def add_hub(self, hub_name):
        if hub_name not in self.hubs:
            self.hubs[hub_name] = []
            print(f"Hub '{hub_name}' added successfully.")
        else:
            print(f"Hub '{hub_name}' already exists.")

    #uc6: add vehicles to hub_name
    def add_vehicle_to_hub(self, hub_name, vehicle):
        if hub_name in self.hubs:
            self.hubs[hub_name].append(vehicle)
            print(f"Vehicle added to hub '{hub_name}'.")
        else:
            print(f"Hub '{hub_name}' does not exist.")

        # UC-7: Duplicate check using list comprehension
        existing_vehicles = self.hubs[hub_name]
        if vehicle in existing_vehicles:
            print(f"Duplicate Vehicle ID '{vehicle.vehicle_id}' not allowed in hub '{hub_name}'.")
            return

        self.hubs[hub_name].append(vehicle)
        print(f"Vehicle '{vehicle.vehicle_id}' added to hub '{hub_name}'.")


    #uc6: display hub_name and vehicles
    def display_hubs(self):
        for hub, vehicles in self.hubs.items():
            print(f"Hub: {hub}, Vehicles Count: {len(vehicles)}")


    #uc8: Search vehicles by hub name
    def search_by_hub(self, hub_name):
        if hub_name not in self.hubs:
            print(f"Hub '{hub_name}' not found.")
            return []

        return self.hubs[hub_name]

    #uc8: Search vehicles with battery > 80%
    def search_by_battery(self, min_battery=80):
        result = []

        for vehicles in self.hubs.values():
            high_battery = list(
                filter(lambda v: v.get_battery_percentage() > min_battery, vehicles)
            )
            result.extend(high_battery)

        return result
    

    #uc9: group vehicle by type
    def group_by_vehicle_type(self):
        grouped = {}

        for vehicles in self.hubs.values():
            for vehicle in vehicles:
                vehicle_type = type(vehicle).__name__

                if vehicle_type not in grouped:
                    grouped[vehicle_type] = []

                grouped[vehicle_type].append(vehicle)

        return grouped
    
    #uc10: Get count of vehicles by status
    def get_status_summary(self):
        summary = {
            "Available": 0,
            "On Trip": 0,
            "Under Maintenance": 0
        }

        for vehicles in self.hubs.values():
            for vehicle in vehicles:
                status = vehicle.get_maintenance_status()
                if status in summary:
                    summary[status] += 1

        return summary
    

    #uc11: alphabetical sort by model
    def sort_vehicles_by_model(self, hub_name):
        if hub_name not in self.hubs:
            print(f"Hub '{hub_name}' not found.")
            return []

        # sorted() with key
        return sorted(self.hubs[hub_name], key=lambda v: v.model)
    
    
    #uc12: Sort vehicles by battery level (highest first)
    def sort_by_battery_desc(self, hub_name):
        if hub_name not in self.hubs:
            print(f"Hub '{hub_name}' not found.")
            return []

        return sorted(
            self.hubs[hub_name],
            key=lambda v: v.get_battery_percentage(),
            reverse=True
        )

    #uc12: Sort vehicles by fare price (highest first)
    def sort_by_fare_desc(self, hub_name, value):
        if hub_name not in self.hubs:
            print(f"Hub '{hub_name}' not found.")
            return []

        return sorted(
            self.hubs[hub_name],
            key=lambda v: v.calculate_trip_cost(value),
            reverse=True
        )
    
    
    # ================= UC-13 : CSV =================
    def save_to_csv(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "hub_name",
                "vehicle_id",
                "model",
                "battery",
                "status",
                "type"
            ])

            for hub, vehicles in self.hubs.items():
                for v in vehicles:
                    writer.writerow([
                        hub,
                        v.vehicle_id,
                        v.model,
                        v.get_battery_percentage(),
                        v.get_maintenance_status(),
                        type(v).__name__
                    ])

        print("Fleet data saved to CSV successfully.")

    def load_from_csv(self, filename):
        if not os.path.exists(filename):
            return   # file not present → first run

        self.hubs.clear()

        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                hub = row["hub_name"]

                if hub not in self.hubs:
                    self.hubs[hub] = []

                if row["type"] == "ElectricCar":
                    vehicle = ElectricCar(
                        row["vehicle_id"],
                        row["model"],
                        int(row["battery"]),
                        5
                    )
                else:
                    vehicle = ElectricScooter(
                        row["vehicle_id"],
                        row["model"],
                        int(row["battery"]),
                        80
                    )

                vehicle.set_maintenance_status(row["status"])
                self.hubs[hub].append(vehicle)

        print("Fleet data loaded from CSV successfully.")

    # ================= UC-14 : JSON =================
    def save_to_json(self, filename):
        data = {}

        for hub, vehicles in self.hubs.items():
            data[hub] = []
            for v in vehicles:
                data[hub].append({
                    "vehicle_id": v.vehicle_id,
                    "model": v.model,
                    "battery": v.get_battery_percentage(),
                    "status": v.get_maintenance_status(),
                    "type": type(v).__name__
                })

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        print("Fleet data saved to JSON successfully.")

    def load_from_json(self, filename):
        if not os.path.exists(filename):
            return

        self.hubs.clear()

        with open(filename, "r") as file:
            data = json.load(file)

        for hub, vehicles in data.items():
            self.hubs[hub] = []

            for v in vehicles:
                if v["type"] == "ElectricCar":
                    vehicle = ElectricCar(
                        v["vehicle_id"],
                        v["model"],
                        v["battery"],
                        5
                    )
                else:
                    vehicle = ElectricScooter(
                        v["vehicle_id"],
                        v["model"],
                        v["battery"],
                        80
                    )

                vehicle.set_maintenance_status(v["status"])
                self.hubs[hub].append(vehicle)

        print("Fleet data loaded from JSON successfully.")