# Sanu K Joseph
n = int(input("Enter a positive integer (n): "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    squares = [i**2 for i in range(1, n+1)]
    print(f"Squares of the first {n} numbers:", squares)