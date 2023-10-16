# Sanu K Joseph
list1 = list(map(int, input("Enter the first list: ").split()))
list2 = list(map(int, input("Enter the second list: ").split()))
print(f"Same length: {len(list1) == len(list2)}")
print(f"Sum of first list: {sum(list1)}")
print(f"Sum of second list: {sum(list2)}")
print(f"Lists sum to the same value: {sum(list1) == sum(list2)}")
print(f"Common value in both lists: {any(item in list1 for item in list2)}")