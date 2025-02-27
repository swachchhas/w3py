def to_title_case(sentence):
 
    words = sentence.split()
    return " ".join(word.capitalize() for word in words)
print("\nTesting to_title_case:")
result = to_title_case("hello world from python")
print(f"to_title_case('hello world from python') = {result}")