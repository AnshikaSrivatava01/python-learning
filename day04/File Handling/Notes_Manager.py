import os

NOTES_FILE = "user_notes.txt"


def add_note():
    note = input("Enter your note: ").strip()
    if note:
        with open(NOTES_FILE, "a", encoding="utf-8") as file:
            file.write(note + "\n")
        print("Note saved.")
    else:
        print("Empty note ignored.")


def view_notes():
    if not os.path.exists(NOTES_FILE):
        print("No notes found.")
        return

    print("\n--- All Notes ---")
    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        notes = [line.strip() for line in file if line.strip()]

    if not notes:
        print("No notes available.")
        return

    for idx, note in enumerate(notes, start=1):
        print(f"{idx}. {note}")


def search_notes():
    if not os.path.exists(NOTES_FILE):
        print("No notes found.")
        return

    query = input("Enter search term: ").strip().lower()
    if not query:
        print("Search term cannot be empty.")
        return

    found = False
    print(f"\n--- Results for '{query}' ---")
    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        for idx, line in enumerate(file, start=1):
            if query in line.lower():
                print(f"Line {idx}: {line.strip()}")
                found = True

    if not found:
        print("No matches found.")


def main():
    while True:
        print("\n=== Notes Manager ===")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            print("Exiting Notes Manager.")
            break
        else:
            print("Invalid choice. Enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()