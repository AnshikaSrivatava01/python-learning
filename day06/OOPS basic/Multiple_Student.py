class StudentRecord:

    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display(self):
        print(f"ID: {self.roll_number} | Name: {self.name:<10} | Marks: {self.marks}")


students = [
    StudentRecord("Sneha", 201, 92),
    StudentRecord("Kunal", 202, 81),
    StudentRecord("Tanya", 203, 74),
]

for s in students:
    s.display()