# Sanu K Joseph
n = int(input("Enter the number of terms: "))
f = [0, 1]
while len(f) < n: f.append(f[-1] + f[-2])
print(f"Fibonacci series of {n} terms:", f)
