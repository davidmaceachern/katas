'''
1603. Design Parking System

https://leetcode.com/problems/design-parking-system/

Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

Implement the ParkingSystem class:

    * `ParkingSystem(int big, int medium, int small)` Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
    * `bool addCar(int carType)` Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.

 

Example 1:

Input
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
Output
[null, true, true, false, false]

Explanation
ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
parkingSystem.addCar(3); // return false because there is no available slot for a small car
parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.


Constraints:

    0 <= big, medium, small <= 1000
    carType is 1, 2, or 3
    At most 1000 calls will be made to addCar


'''

'''
Initial Attempt 152 ms


class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.parkedCars = {
            1: { 'capacity': big, 'occupied': 0 },
            2: { 'capacity': medium, 'occupied': 0 },
            3: { 'capacity': small, 'occupied': 0 } 
        }

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.parkedCars[carType]['occupied'] < self.parkedCars[carType]['capacity']:
            print('There is capacity')
            self.parkedCars[carType]['occupied'] += 1
            return True    
        return False 
'''

'''
Solution that is faster at 124ms...

class ParkingSystem:
	def __init__(self, big, medium, small):
		self.big_spots = big
		self.med_spots = medium
		self.small_spots = small


	def addCar(self, carType):
		if carType == 1:
			if self.big_spots > 0: # if there is enough spots
				self.big_spots -= 1 # remove 1 big spot
				return True   
			else:  # if not enough spots return false to indicate no spots
				return False 
		if carType == 2:
			if self.med_spots > 0:
				self.med_spots -= 1
				return True
			else:
				return False
		else:  # if carType isn't 1 or 2 its 3 and small
			if self.small_spots > 0:
				self.small_spots -= 1
				return True
			else:
				return False
'''

# Solution that uses more memory but less time 132 ms

class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.capacity = {"1": big, "2": medium, "3": small}                

    def addCar(self, carType):        
        if self.capacity[str(carType)] - 1 >= 0:
            self.capacity[str(carType)] -= 1
            return True        
        return False

