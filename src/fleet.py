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

    def display_hubs(self):
        for hub, vehicles in self.hubs.items():
            print(f"Hub: {hub}, Vehicles Count: {len(vehicles)}")
