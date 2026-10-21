filename = "daily_notes.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print("--- File Contents ---")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")