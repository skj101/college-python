user_input = input("Enter a string: ")
print("Modified string:", user_input[0] + user_input[1:].replace(user_input[0], '$'))