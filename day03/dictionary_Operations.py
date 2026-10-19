d = {x: x*x for x in range(1, 11)}
print("Squares (1 to 10):", d)

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))
nums = [1, 2, 3, 2, 4, 1, 5]
print("List after removing duplicates:", remove_duplicates(nums))

def get_second_largest(lst):
    unique= list(set(lst))
    if len(unique) < 2:
        return None
    unique.sort(reverse=True)
    return unique[1]
val = [10, 20, 4 ,45, 99, 99, 45]
print("Second largest value:", get_second_largest(val))

def merge_and_sum_dicts(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        merged[key] = merged.get(key, 0) + value
    return merged    
sales1= {"apples": 10, "bananas": 5, "oranges": 8}
sales2= {"bananas": 12, "oranges": 4, "grapes": 15}
print(merge_and_sum_dicts(sales1, sales2))

def count_frequency(items):
    frequency = {}
    for item in items:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency
letters = ['a', 'b', 'a', 'c', 'b', 'a']
print("Frequency of letters:", count_frequency(letters))

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

union = set_a | set_b
intersection = set_a & set_b
difference = set_a - set_b

print(f"Union: {union}")
print(f"Intersection: {intersection}")
print(f"Difference: {difference}")

def tuple_to_dict(tup):
    result = {}
    for key, val in tup:
        result.setdefault(key, []).append(val)
    return result
pairs = [("cat", "meow"), ("dog", "bark"), ("cat", "purr")]
print(tuple_to_dict)

def group_by_first_letter(words):
    groups = {}
    for word in words:
        if not word: 
            continue
        first_letter = word[0].lower()
        groups.setdefault(first_letter, []).append(word)
    return groups    
word_list = ["Apple", "banana", "avocado", "cherry", "Blueberry"]
print(group_by_first_letter(word_list))

def top_student(records):
    highest_avg = -1
    best_student = None

    for name, marks in records.items():
        if not marks:
            continue
        avg = sum(marks) / len(marks)
        if avg > highest_avg:
            highest_avg = avg
            best_student = name

    return best_student, highest_avg

students = {
    "Rahul": [85, 90, 78],
    "Ananya": [92, 95, 89],
    "Vikram": [70, 80, 75]
}
name, avg = top_student(students)
print(f"{name} has the highest average: {avg:.2f}") 

def total_by_category(transactions):
    totals = {}
    for t in transactions:
        category = t["category"]
        amount = t["amount"]
        totals[category] = totals.get(category, 0) + amount
    return totals


records = [
    {"category": "Food", "amount": 250},
    {"category": "Transport", "amount": 100},
    {"category": "Food", "amount": 400},
    {"category": "Utilities", "amount": 1200},
    {"category": "Transport", "amount": 150}
]
print(total_by_category(records))
