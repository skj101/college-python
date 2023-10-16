# Sanu K Joseph
count_a_in_names = lambda names: sum(name.lower().count('a') for name in names)
names = input("Enter a list of names : ").split()
print(f"Total occurrences of 'a': {count_a_in_names(names)}")
