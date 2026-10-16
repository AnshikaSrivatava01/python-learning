def calculate_average(*marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)

def info_user(name, *marks):
   profile = {"name": name, "average": calculate_average(*marks)}
   return profile

profile = info_user("Alice", 85, 90, 78, 92)
print(f"Profile: {profile}")
print(f"Average marks: {profile['average']:.2f}")