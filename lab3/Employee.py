import re
from person import Person
from car import Car
class Employee(Person):
    def __init__(self,name,money,id,distanceToWork):
        super(Employee,self).__init__(name,money)
        self.id = id
        self._car = None
        self.__email = None
        self.__salary = 1000
        self.distanceToWork = distanceToWork

    def __str__(self):
        return "Nothing"

    def work(self,hours):
        if hours == 8:
            self._mood = "Happy"
        elif hours > 7:
            self._mood = "Tired"
        else:
            self._mood = "Lazy"

    def drive(self, distance):
        if self._car.fuelRate == 0:
            self.refuel()
        self._car.run(distance, self._car.velocity)

    def refuel(self,gasAmount=100):
        self._car.fuelRate(gasAmount)

    @property
    def car(self):
        return self._car

    @car.setter
    def car(self, car):
        self._car = car

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if re.fullmatch("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+",email):
            self.__email = email
        else:
            self.__email = "none"

    @property
    def salary(self):
        return self.__salary

    @email.setter
    def salary(self, salary):
        if salary > 1000:
            self.__salary = salary
