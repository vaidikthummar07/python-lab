n = int(input("Enter the number of Fibonacci terms: "))

# First two terms of Fibonacci sequence
a, b = 0, 1

# Print the Fibonacci sequence
for _ in range(n):
    print(a)
    a, b = b, a + b  # Update a and b to the next two Fibonacci numbers
