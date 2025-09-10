from typing import List
import math

class Coordinate:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Landmark:
    def __init__(self, name: str, location: Coordinate):
        self.name = name
        self.location = location

class Road:
    def __init__(self, name: str, polyline: List[Coordinate]):
        self.name = name
        self.polyline = polyline

class Map:
    def __init__(self):
        self.roads: List[Road] = []
        self.landmarks: List[Landmark] = []

    def add_road(self, road: Road):
        self.roads.append(road)

    def add_landmark(self, landmark: Landmark):
        self.landmarks.append(landmark)

    def get_nearby_landmarks(self, coord: Coordinate, radius: float) -> List[Landmark]:
        nearby = []
        for landmark in self.landmarks:
            coordinate = [coord.x, coord.y]
            landmark_coord = [landmark.location.x, landmark.location.y]
            dist = math.dist(coordinate, landmark_coord)
            if dist <= radius:
                nearby.append(landmark)

        return nearby

class Robot:
    def __init__(self, start_pose: Coordinate, map_obj: Map):
        self.__pose = start_pose
        self.map = map_obj

    def move(self, dx: float, dy: float):
        self.__pose.x += dx
        self.__pose.y += dy
    
    def get_pose(self) -> Coordinate:
        return self.__pose

    def sense(self, radius: float) -> List[Landmark]:
        return self.map.get_nearby_landmarks(self.__pose, radius)

class DeliveryRobot(Robot):
    def __init__(self, start_pose, map_obj):
        super().__init__(start_pose, map_obj)
    
    def deliver_package(self) -> None:
        print("Delivered Package")

# Example usage:
city_map = Map()
city_map.add_landmark(Landmark("Stop Sign", Coordinate(5, 5)))
robot = DeliveryRobot(Coordinate(0, 0), city_map)
robot.move(3, 4)
nearby = robot.sense(radius=5)
print([lm.name for lm in nearby])
robot.deliver_package()

# Tasks for You

# Implement Robot.move() so it correctly updates the private __pose.

# Implement Map.get_nearby_landmarks() using distance formula.

# Implement Robot.sense() by calling Map.get_nearby_landmarks() with the robot’s current pose.

# Create a subclass DeliveryRobot that adds a method deliver_package() that prints something like "Delivered package at x,y".

# Bonus: extend Coordinate to 3D, and update distance calculations.