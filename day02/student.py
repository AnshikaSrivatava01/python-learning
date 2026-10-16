students = [
    {"name": "Aman", "marks": 82},
    {"name": "Pooja", "marks": 68},
    {"name": "Rohit", "marks": 91},
    {"name": "Sneha", "marks": 75},
    {"name": "Karan", "marks": 62},
]

filtered_students = list(filter(lambda student: student["marks"] > 70, students))
sorted_students = sorted(filtered_students, key=lambda student: student["marks"], reverse=True)
print("Students with marks greater than 70, sorted by marks (descending):")
for student in sorted_students:
    print(f"Name: {student['name']}, Marks: {student['marks']}")    