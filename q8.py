def char_count(s):
    char_dict = {}
    for char in s:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict
print("\nTesting char_count:")
result = char_count("hello")
print(f"count('hello') =",result)