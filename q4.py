def largest_word(sentence):
    """
    Find the longest word in a sentence.
    """
    words = sentence.split()
    if not words:
        return None
    
print("\nTesting largest_word:")
result = largest_word("Python programming is awesome")
print(f"largest_word('Python programming is awesome') = {result}") 