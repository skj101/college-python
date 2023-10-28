# Sanu K Joseph
def compare():
    list1 = list(map(int, input("Enter the first list: ").split()))
    list2 = list(map(int, input("Enter the second list: ").split()))
    same_length = len(list1) == len(list2)
    sum1 = sum(list1)
    sum2 = sum(list2)
    same_sum = sum1 == sum2
    any_common = any(item in list1 for item in list2)
    return same_length, sum1, sum2, same_sum, any_common
result = compare()
print(f"Same length: {result[0]}")
print(f"Sum of first list: {result[1]}")
print(f"Sum of second list: {result[2]}")
print(f"Lists sum to the same value: {result[3]}")
print(f"Common value in both lists: {result[4]}")
