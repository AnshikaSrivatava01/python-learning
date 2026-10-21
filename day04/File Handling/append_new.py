new_entry = "Day 2:\n- Explored read(), readline(), and readlines().\n"

with open("daily_notes.txt", "a", encoding="utf-8") as file:
    file.write(new_entry)

print("New entry appended successfully.")