notes = """Day 1:
- Learned about open() and file handling modes.
- Understood why the 'with' statement is safe.
- Practiced writing strings to disk.
"""

with open("daily_notes.txt", "w", encoding="utf-8") as file:
    file.write(notes)

print("Notes written successfully to daily_notes.txt.")