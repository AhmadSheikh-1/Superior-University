punctations = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
string = input("Enter a string: ")
string = string.lower()
for char in string:
    if char in punctations:
        string = string.replace(char, " " )
print(string)
