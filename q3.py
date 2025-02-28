def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
print("\nTesting multiplication_table:")
print("multiplication_table(5):")
multiplication_table(5)