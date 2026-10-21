source_file = "daily_notes.txt"
destination_file = "daily_notes_backup.txt"

try:
    with open(source_file, "r", encoding="utf-8") as src:
        with open(destination_file, "w", encoding="utf-8") as dest:
            for line in src:
                dest.write(line)

    print(f"Copied contents from '{source_file}' to '{destination_file}'.")

except FileNotFoundError:
    print(f"Error: Source file '{source_file}' not found.")