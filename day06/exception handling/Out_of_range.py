class InvalidMarksError(Exception):
    def __init__(self, marks):
        super().__init__(
            f"Invalid score: {marks}. Marks must be between 0 and 100."
        )

def validate_student_marks(marks):
    if not (0 <= marks <=100):
        raise InvalidMarksError(marks)
    return marks

try: 
    score = int(input("Enter your score:"))
    validate_student_marks(score)
except InvalidMarksError as e:
    print(e)            