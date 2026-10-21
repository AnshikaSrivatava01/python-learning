from datetime import datetime

now = datetime.now()

formatted_date = now.strftime("%Y-%m-%d")
formatted_time = now.strftime("%H:%M:%S")
day_of_week = now.strftime("%A")

print(f"Date: {formatted_date}")
print(f"Time: {formatted_time}")
print(f"Day : {day_of_week}")