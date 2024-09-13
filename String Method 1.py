#Length Method: Determines the amount of characters in a string (includes spaces and special characters)
name = "turner"
print(len(name))
#Find: located the first index of a character
print(name.find ("e"))
#Capitalize
print(name.capitalize())
#lower
print (name.lower())
#isdigit: Determines if any of the characters in the string are a digit (numbers)
print(name.isdigit())
#isalpha: Determines if all of the characters are alphabetical (returns false if a space is included)
print (name.isalpha())
#Count: number of  specified characters in string
print(name.count("r"))
#Replace: replaces characters in a string at specified locations or by type
print(name.replace("r","j"))
#String Algebra: Allows for the usage of algebraic functions to influence the output of the print function
print(name*3)

