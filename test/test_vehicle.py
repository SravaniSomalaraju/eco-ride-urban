import pytest
from src.vehicle import ElectricCar, ElectricScooter

@pytest.fixture
def car():
    return ElectricCar("C101","Tesla", 90, "Available", 500, 5)
@pytest.fixture
def scooter():
    return ElectricScooter("D101", "Ola", 70, "Available", 100, 80)

def test_vehicle_creation(car):
    assert car.vehicle_id == "C101"
    assert car.model == "Tesla"
    assert car.battery_percentage == 90
@pytest.mark.parametrize(
    "battery", [0,50,100]
)

def test_valid_battery_perc(car, battery):
    car.battery_percentage = battery
    assert car.battery_percentage == battery

def test_invalid_battery_perc(capsys, car):
    car.battery_percentage = 150
    captured = capsys.readouterr()
    assert "Battery percentage must be between 0 and 100" in captured.out

@pytest.mark.parametrize(
    "distance, expected", [(10, 10.0), (20, 15.0)]

)

def test_car_trip_cost(car, distance, expected):
    assert car.calculate_trip_cost(distance) == expected

@pytest.mark.parametrize(
    "minutes, expected", [(10, 2.5), (20, 4.0)]
)

def test_scooter_trip_cost(scooter, minutes, expected):
    assert scooter.calculate_trip_cost(minutes) == expected