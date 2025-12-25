class FleetManager:
    def __init__(self):
        # Dictionary: Hub Name -> List of Vehicles
        self.hubs = {}

    def add_hub(self, hub_name):
        if hub_name not in self.hubs:
            self.hubs[hub_name] = []
            print(f"Hub '{hub_name}' added successfully.")
        else:
            print(f"Hub '{hub_name}' already exists.")

    def add_vehicle_to_hub(self, hub_name, vehicle):
        if hub_name in self.hubs:
            self.hubs[hub_name].append(vehicle)
            print(f"Vehicle added to hub '{hub_name}'.")
        else:
            print(f"Hub '{hub_name}' does not exist.")

        #check duplicates
        if vehicle in self.hubs[hub_name]:
            print(f"Duplicate Vehicle ID '{vehicle.vehicle_id}' not allowed.")
            return

        self.hubs[hub_name].append(vehicle)
        print(f"Vehicle '{vehicle.vehicle_id}' added to hub '{hub_name}'.")

    def display_hubs(self):
        for hub, vehicles in self.hubs.items():
            print(f"Hub: {hub}, Vehicles Count: {len(vehicles)}")

    # Search vehicles by hub name
    def search_by_hub(self, hub_name):
        if hub_name not in self.hubs:
            print(f"Hub '{hub_name}' not found.")
            return []

        return self.hubs[hub_name]

    # Search vehicles with battery > 80%
    def search_by_battery(self, min_battery=80):
        result = []

        for vehicles in self.hubs.values():
            high_battery = list(
                filter(lambda v: v.get_battery_percentage() > min_battery, vehicles)
            )
            result.extend(high_battery)

        return result
    #group vehicle by type
    def group_by_vehicle_type(self):
        grouped = {}

        for vehicles in self.hubs.values():
            for vehicle in vehicles:
                vehicle_type = type(vehicle).__name__

                if vehicle_type not in grouped:
                    grouped[vehicle_type] = []

                grouped[vehicle_type].append(vehicle)

        return grouped
    
    # Get count of vehicles by status
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
    

    #11
    def sort_vehicles_by_model(self, hub_name):
        if hub_name not in self.hubs:
            print(f"Hub '{hub_name}' not found.")
            return []

        # sorted() with key
        return sorted(self.hubs[hub_name], key=lambda v: v.model)

