class StudentWithGrade:

    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "F"

    def display_details(self):
        print(
            f"Student: {self.name} | Roll: {self.roll_number} | Marks: {self.marks} | Grade: {self.get_grade()}"
        )


s = StudentWithGrade("Rohit", 102, 78)
s.display_details()