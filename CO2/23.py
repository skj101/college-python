# Sanu K Joseph
num1 = int(input("Please enter the first 4-digit number: "))
num2 = int(input("Please enter the second 4-digit number: "))

def is_perfect_square(n):
    return n**0.5 % 1 == 0

def all_even_digits(n):
    return all(int(digit) % 2 == 0 for digit in str(n))

perfect_even_squares = [i for i in range(num1, num2+1) if is_perfect_square(i) and i % 2 == 0 and all_even_digits(i)]

print(f"Perfect even squares with even digits between {num1} and {num2} are: {perfect_even_squares}")