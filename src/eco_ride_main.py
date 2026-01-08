from vehicle import ElectricCar, ElectricScooter
from fleet import FleetManager
class EcoRideMain:
    @staticmethod
    def main():
        print("Welcome to Eco-Ride Urban Mobility System")

        fleet = FleetManager()

        
        fleet.load_from_csv("src/fleet.csv")
        fleet.load_from_json("src/fleet.json")

       
        if not fleet.hubs:
            fleet.hubs["Downtown"] = []

            car = ElectricCar("C101", "Tesla Model 3", 85, 5)
            scooter = ElectricScooter("S102", "Ather 450X", 90, 80)

            fleet.hubs["Downtown"].append(car)
            fleet.hubs["Downtown"].append(scooter)

        
        fleet.save_to_csv("src/fleet.csv")
        fleet.save_to_json("src/fleet.json")

           
if __name__ == "__main__":
    EcoRideMain.main()
