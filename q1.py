def count_vowels(text):
  
    vowels = 'aeiou'
    return sum(1 for char in text.lower() 
               if char in vowels)
print("Testing count_vowels:")
result = count_vowels("Hello World")
print("count_vowels('Hello World') =", result) 