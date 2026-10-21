filename = "daily_notes.txt"
line_cnt = 0
word_cnt = 0
char_cnt = 0

try:
    with open(filename, "r", encoding = "utf-8") as file:
        for line in file:
            line_cnt += 1
            words = line.split()
            word_cnt += len(words)
            char_cnt += len(line)
    print(f"Line count: {line_cnt}")
    print(f"Word count: {word_cnt}")
    print(f"Character count: {char_cnt}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")