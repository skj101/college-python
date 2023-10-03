get_numbers = lambda: ["over" if int(x) > 100 else int(x) for x in input("Enter numbers separated by spaces: ").split()]
a = get_numbers()
print(a)
