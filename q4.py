def largest_word(sentence):

    words = sentence.split()
    if not words:
        return None
    
print("\nTesting largest_word:")
result = largest_word("Python programming is awesome")
print("largest_word('Python programming is awesome')=",result) 