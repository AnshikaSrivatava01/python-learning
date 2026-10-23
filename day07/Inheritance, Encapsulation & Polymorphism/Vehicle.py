class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        return f"{self.make} {self.model}"


class ElectricCar(Vehicle):
    def __init__(self, make, model, battery_capacity_kwh):
        super().__init__(make, model)
        self.battery_capacity_kwh = battery_capacity_kwh

    def info(self):
        return f"{super().info()} ({self.battery_capacity_kwh} kWh battery)"


ev = ElectricCar("Tata", "Nexon EV", 40.5)
print(ev.info())