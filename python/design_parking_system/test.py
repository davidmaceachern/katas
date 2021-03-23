from solution import ParkingSystem

def test_parking_system():
    """
    Test that it can check if a car can park
    """

    parkingSystem = ParkingSystem(1,1,0)

    assert parkingSystem.addCar(1) == True
    assert parkingSystem.addCar(2) == True
    assert parkingSystem.addCar(3) == False 
    assert parkingSystem.addCar(1) == False 