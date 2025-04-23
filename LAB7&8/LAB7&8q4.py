class Employee:
    def __init__(self, emp_name, emp_salary):
        self.emp_name = emp_name
        self.emp_salary = emp_salary

    def __add__(self, other):
        total_salary = self.emp_salary + other.emp_salary
        return Employee(f"{self.emp_name} & {other.emp_name}", total_salary)

    def __sub__(self, other):
        salary_difference = abs(self.emp_salary - other.emp_salary)
        return salary_difference

    def display(self):
        return f"Employee: {self.emp_name}, Salary: {self.emp_salary}"

e1 = Employee("John", 5000)
e2 = Employee("Doe", 7000)
e3 = e1 + e2
print(e3.display())
print(e1 - e2)
