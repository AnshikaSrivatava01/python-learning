class Employee:
    def __init__(self, name, base_pay):
        self.name = name
        self.base_pay = base_pay

    def calculate_salary(self):
        return self.base_pay


class FullTimeEmployee(Employee):
    def __init__(self, name, base_pay, bonus):
        super().__init__(name, base_pay)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_pay + self.bonus


class Contractor(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, base_pay=0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


ft = FullTimeEmployee("Rohan", 60000, 12000)
ct = Contractor("Kiran", 800, 45)

print(f"{ft.name}'s Salary: Rs. {ft.calculate_salary()}")
print(f"{ct.name}'s Salary: Rs. {ct.calculate_salary()}")