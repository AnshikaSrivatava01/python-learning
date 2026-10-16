numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)

words = ["python", "code", "list"]
uppercase_words = [word.upper() for word in words]
print("Uppercase words:", uppercase_words)

num = [3, 7, 12, 18, 25]
doubled_num = list(map(lambda x: x * 2, num))
print("Doubled numbers:", doubled_num)

val = [12, 55, 34, 78, 90, 50, 49, 102]
new_val = list(filter(lambda x: x > 50, val))
print("Numbers greater than 50:", new_val)

student_records = [("Alice", 82), ("Bob", 95), ("Charlie", 74), ("Diana", 91)]
sorted_records = sorted(student_records, key=lambda student: student[1], reverse=True)
print("Sorted by marks (descending):", sorted_records)

items = ["apple", "banana", "kiwi", "pomegranate"]
word_lengths = {item: len(item) for item in items}
print("Word lengths:", word_lengths)