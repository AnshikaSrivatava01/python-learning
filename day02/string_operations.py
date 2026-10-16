import string

def anagram_check(str1, str2) -> bool:
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)
print(anagram_check("Listen", "Silent"))

def first_unique_char(s: str) -> int:
    s = s.lower()
    for i, char in enumerate(s):
        if s.count(char) == 1:
            return i
    return -1
print(first_unique_char("hello"))

def is_palindrome(s: str) -> bool:
    s = s.lower()
    s = ''.join(char for char in s if char in string.ascii_lowercase)
    return s == s[::-1]
print(is_palindrome("A man a plan a canal Panama"))

def remove_duplicates(s: str) -> str:
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)
print(remove_duplicates("programming"))

def count_word_frequency(s: str) -> dict:
    words = s.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

print(count_word_frequency("the quick brown fox jumps over the lazy dog"))  

def is_all_digits(s: str) -> bool:
    return s.isdigit()  

print(is_all_digits("12345"))  
print(is_all_digits("123a45"))  

def count_vowels_consonants(s: str) -> tuple:
    vowels = set("aeiou")
    s = s.lower()
    vowel_count = sum(1 for char in s if char in vowels)
    consonant_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    return vowel_count, consonant_count            
print(count_vowels_consonants("Hello World"))