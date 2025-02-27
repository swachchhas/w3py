def multiplication_table(n):
    """
    Print multiplication table for number n from 1 to 10.
    """
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
print("\nTesting multiplication_table:")
print("multiplication_table(5):")
multiplication_table(5)