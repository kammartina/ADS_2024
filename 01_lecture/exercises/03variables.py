"""
Assign your name to a variable and print it.
"""
name = "Martina"
print(name)

"""
Assign your age to a variable and print it.
"""
age = 25
print(age)

"""
Assign values 5, 10, and 15 to three variables and print their sum.
Prints:
    Sum: 25
"""
#Solution_1:
num1 = 5
num2 = 10
num3 = 15
sum = 5 + 10 + 15
print("Sum:", sum)
#it can‘t be print("Sum" + sum) because I would mix up a string with an integer

#Solution_2:
num = 5, 10, 15
sum = 5 + 10 + 15
print("Sum:", sum)

"""
Assign an integer to a variable and print its type
"""
int = 20
print(type(int))

#if I want to print the type of more than just one thing
name = "Ivana"
int = 20
print(type(name),type(int))

"""
Assign a floating-point number to a variable and print its type
"""
num = 3.6
print(type(num))

"""
Convert the integer from before to a string and print its type
"""
#INTEGER is just a number
#it is a STRING if I use " "
num = "20"
print(type(num))
