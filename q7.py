def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]
print("\nTesting is_palindrome:")
result1 = is_palindrome("madam")
result2 = is_palindrome("hello")
print(f"is_palindrome('madam') = {result1}")  
print(f"is_palindrome('hello') = {result2}")