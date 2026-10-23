class Employee:
    def __init__(self, emp_id, name, base_rate):
        self._emp_id = emp_id
        self.name = name
        self.base_rate = base_rate

    def calculate_pay(self):
        return self.base_rate

    def get_summary(self):
        return f"[{self._emp_id}] {self.name} | Pay: Rs. {self.calculate_pay():,.2f}"


class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary, performance_bonus=0):
        super().__init__(emp_id, name, monthly_salary)
        self.performance_bonus = performance_bonus

    def calculate_pay(self):
        return self.base_rate + self.performance_bonus


class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name, hourly_rate)
        self.hours_worked = hours_worked

    def calculate_pay(self):
        regular_hours = min(40, self.hours_worked)
        overtime_hours = max(0, self.hours_worked - 40)
        return (regular_hours * self.base_rate) + (overtime_hours * self.base_rate * 1.5)


class EmployeeRegistry:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        if not isinstance(emp, Employee):
            raise TypeError("Object must inherit from Employee.")
        self.employees.append(emp)

    def total_payroll(self):
        return sum(emp.calculate_pay() for emp in self.employees)

    def list_all(self):
        for emp in self.employees:
            print(emp.get_summary())

registry = EmployeeRegistry()
registry.add_employee(SalariedEmployee("EMP101", "Amit Kumar", 75000, 10000))
registry.add_employee(HourlyEmployee("EMP102", "Priya Singh", 600, 48))
registry.add_employee(SalariedEmployee("EMP103", "Rahul Sharma", 52000))

print("=== Employee Payroll List ===")
registry.list_all()
print("-" * 35)
print(f"Total Company Payroll: Rs. {registry.total_payroll():,.2f}")