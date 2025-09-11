
# Multiple levels - > multiple floors


# Floors
# Vechicles:  -> cars -> motorcycles - > Trucks
# Parking spot : types of vechiles
# Availability of parking spots

# Are there any specific constraints or limitations?
# Who are the primary users of this system?
# What if users park in  the wrong spot and the spot is occupied.

# Main entities:
# - Floors
# - Parking spots
# - Vechicles
# overall system - Parking monitor

# Enum VechicleSize:
# small, medium big

# ParkingSpots
# - id: int
# - type: VechicleSize
# - available: bool

# Vechicle
# - lisence_id
# - size: VechicleSize

# Floors:
# -  spotsAvailable: int
# - spots : dict[Spots]



from enum import Enum

class VehicleSize(Enum):
    SMALL = 1
    MEDIUM = 2
    BIG = 3

class ParkingException(Exception):
    pass

class ParkingSpot:
    def __init__(self, id: str, size: VehicleSize, availability: bool = True):
        self.id = id
        self.size = size
        self._availability = availability
        self.vehicle = None

    def set_occupied(self, vehicle):
        if not self._availability:
            raise ParkingException(f"Spot {self.id} is already occupied.")
        if not self.fits(vehicle.size):
            raise ParkingException(f"Vehicle {vehicle.license_id} does not fit in spot {self.id}.")
        self._availability = False
        self.vehicle = vehicle

    def remove_vehicle(self):
        self._availability = True
        self.vehicle = None

    def get_availability(self) -> bool:
        return self._availability

    def fits(self, vehicle_size: VehicleSize) -> bool:
        return self._availability and vehicle_size.value <= self.size.value


class Vehicle:
    def __init__(self, license_id: str, size: VehicleSize):
        self.license_id = license_id
        self.size = size

class Car(Vehicle):
    def __init__(self, license_id):
        super().__init__(license_id, VehicleSize.MEDIUM)

class Bus(Vehicle):
    def __init__(self, license_id):
        super().__init__(license_id, VehicleSize.BIG)

class Motorcycle(Vehicle):
    def __init__(self, license_id):
        super().__init__(license_id, VehicleSize.SMALL)


class Floor:
    def __init__(self, id: str):
        self.id = id
        self.spots = []

    def add_spot(self, spot: ParkingSpot):
        self.spots.append(spot)

    def get_available_spots(self, size: VehicleSize):
        return [s for s in self.spots if s.fits(size)]

    


        


