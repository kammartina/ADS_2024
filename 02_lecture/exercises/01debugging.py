"""
The following program contains several syntactic errors.
Remove the comments and fix the program so that the syntax is in order and the program works as specified by the examples below.

Example 1:
    Please type in a number: 13
    13 must be my lucky number!
    Have a nice day!

Example 2:
    Please type in a number: 101
    The number was greater than one hundred
    Now its value has decreased by one hundred
    Its value is now 1
    1 must be my lucky number!
    Have a nice day!
"""
number = int(input("Please type in a number: "))

if number > 100:
    print("The number was greater than one hundred")
    print("Now its value has decreased by one hundred")
    print(f"Its value is now {number}")
    print(f"{number} must be my lucky number!")
    print("Have a nice day!")
else:
    print(f"{number} must be my lucky number!")
    print("Have a nice day!")