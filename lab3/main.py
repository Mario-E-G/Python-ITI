from person import Person
from Employee import Employee
from office import Office

employees = []
employees.append(Employee("mario",10000,10,200))
employees.append(Employee("ehab",10000,10,200))


of1=Office("it",employees)
print(of1.get_All_employees())



