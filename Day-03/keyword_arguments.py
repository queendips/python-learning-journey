# Keyword arguments pass values to a function using parameter names instead of positions.
def employee(name, department, salary):
    print("Name:", name)
    print("Department:", department)
    print("Salary:", salary)

employee(
    salary=50000,
    name="Bob",
    department="DevOps"
)