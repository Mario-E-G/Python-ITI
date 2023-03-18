import math


class Car:
    def __init__(self, name):
        self.name = name
        self.__fuelRate = 100
        self.__velocity = 0

    def stop(self):
        self.__velocity = 0
        if self.__fuelRate > 0:
            print("The destintation: ")
        else:
            print("distance: " + abs(self.__fuelRate))

    def run(self, distance, velocity):
        self.__velocity = velocity
        self.__fuelRate = self.__fuelRate - distance
        self.stop()

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def car(self, velocity):
        if velocity < 0 and velocity > 200:
            self.__velocity = 0
        else:
            self.__velocity = velocity

    @property
    def fuelRate(self):
        return self.__fuelRate

    @fuelRate.setter
    def fuelRate(self, fuelAmount):
        self.__velocity = fuelAmount
