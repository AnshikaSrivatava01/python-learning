filename = "daily_notes.txt"
search_word = input("Enter the word to search: ")
cnt = 0

try:
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            words = line.split()
            cnt += words.count(search_word)
    print(f"The word '{search_word}' appears {cnt} times in the file.")
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")