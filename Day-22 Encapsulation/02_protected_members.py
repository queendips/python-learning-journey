# Protected members start with a single underscore (_).
class Employee:

    def __init__(self, salary):
        self._salary = salary

emp = Employee(50000)

print(emp._salary)