class Employee:

    def __init__(self, emp_id, name, monthly_salary):
        self.emp_id = emp_id
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_annual_salary(self):
        return self.monthly_salary * 12


emp = Employee("E104", "Pooja", 45000)
print(f"Employee: {emp.name}")
print(f"Annual Salary: Rs. {emp.calculate_annual_salary()}")