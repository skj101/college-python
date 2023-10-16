# Sanu K Joseph
string = input("Enter random string : ")
if len(string) >= 3:
    string += 'ly' if string.endswith('ing') else 'ing'
print(string)