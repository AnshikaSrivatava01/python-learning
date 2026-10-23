class Employee:
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def get_role(self):
        return "Employee"

class Manager(Employee):
    def __init__(self, emp_id, name, base_salary, team_size):
        super().__init__(emp_id, name, base_salary)
        self.team_size = team_size

    def get_role(self):
        return f"Manager leading a team of {self.team_size}"

class Developer(Employee):
    def __init__(self, emp_id, name, base_salary, programming_language):
        super().__init__(emp_id, name, base_salary)
        self.tech_stack = programming_language

    def get_role(self):
        return f"Developer working with {', '.join(self.tech_stack)}"

mgr = Manager("M01", "Arun", 85000, 8)
dev = Developer("D02", "Neha", 65000, ["Python", "FastAPI", "React"])

print(f"{mgr.name}: {mgr.get_role()}")
print(f"{dev.name}: {dev.get_role()}")
    