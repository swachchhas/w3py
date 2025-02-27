def sum_of_list(numbers):
    """
    Calculate sum of all numbers in a list without using sum().
    """
    total = 0
    for num in numbers:
        total += num
    return total
print("\nTesting sum_of_list:")
result = sum_of_list([1, 2, 3, 4, 5])
print(f"sum_of_list([1, 2, 3, 4, 5]) = {result}") 

