import pytest
from src.fleet import *
from src.vehicle import *

@pytest.fixture
def fleet_manager():
    manager = FleetManager()
    manager.add_hub("Downtown")
    return manager

@pytest.fixture
def vehicles():
    car = ElectricCar("C101","Tesla", 90, "Available", 500, 5)
    scooter = ElectricScooter("D101", "Ola", 70, "Available", 100, 80)
    return car, scooter

def test_add_hub(capsys):
    manager = FleetManager()
    manager.add_hub("Airport")
    captured = capsys.readouterr()
    assert "Hub 'Airport' added successfully." in captured.out

def test_duplicate_vehicle(capsys, fleet_manager, vehicles):
    car, _ = vehicles
    fleet_manager.add_vehicle_to_hub("Downtown", car)
    fleet_manager.add_vehicle_to_hub("Downtown", car)

    captured = capsys.readouterr()
    assert "Duplicate vehicle ID not allowed" in captured.out

def test_search_by_battery(fleet_manager, vehicles):
    car, scooter = vehicles
    fleet_manager.add_vehicle_to_hub("Downtown", car)
    fleet_manager.add_vehicle_to_hub("Downtown", scooter)

    result = fleet_manager.search_by_battery(80)
    assert len(result) == 1
    assert result[0].vehicle_id == "C101"

def test_group_by_vehicle_type(fleet_manager, vehicles):
    car, scooter = vehicles
    fleet_manager.add_vehicle_to_hub("Downtown", car)
    fleet_manager.add_vehicle_to_hub("Downtown", scooter)

    grouped = fleet_manager.group_by_vehicle_type()
    assert "ElectricCar" in grouped
    assert "ElectricScooter" in grouped
    assert len(grouped["ElectricCar"]) == 1
    assert len(grouped["ElectricScooter"]) == 1


def test_sort_by_model(fleet_manager):
    car1 = ElectricCar("C1", "Tesla", 80, "available", 100, 5)
    car2 = ElectricCar("C2", "Audi", 90, "available", 100, 5)

    fleet_manager.add_vehicle_to_hub("Downtown", car1)
    fleet_manager.add_vehicle_to_hub("Downtown",car2)

    sorted_list = fleet_manager.sort_vehicles_by_model("downtown")
    assert sorted_list[0].model == "Audi"