def sum_of_list(numbers):
  
    total = 0
    for num in numbers:
        total += num
    return total
print("\nTesting sum_of_list:")
result = sum_of_list([1, 2, 3, 4, 5])
print(f"sum_of_list([1, 2, 3, 4, 5]) = {result}") 

