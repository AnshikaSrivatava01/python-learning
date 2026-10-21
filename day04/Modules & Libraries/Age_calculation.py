from datetime import date

dob_year = int(input("Enter your birth year (YYYY): "))
dob_month = int(input("Enter your birth month (MM): ")) 
dob_day = int(input("Enter your birth day (DD): "))

birth_date = date(dob_year, dob_month, dob_day)
today = date.today()

has_had_birthday = (today.month, today.day) >= (birth_date.month, birth_date.day)
age = today.year - birth_date.year - (1 if not has_had_birthday else 0)
print(f"You are {age} years old.")