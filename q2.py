def find_maximum(list1):
    if not list1:
        return None
    
    maximum = list1[0]
    for num in list1[1:]:
        if num > maximum:
            maximum = num
    return maximum
print("\nTesting find_maximum:")
result = find_maximum([10, 25, 5, 80, 30])
print(f"find_maximum([10, 25, 5, 80, 30]) = {result}")