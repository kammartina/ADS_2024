"""
Exercises "Functions"
"""
"""
RETURN
"""
def sum(x,y):
    result = x + y
    return result
sum(1,2)


def smallest(a,b):
    if a < b:
        return a #if a is not smaller than b, this step will be skipped and program continues to the next line (return b)
    return b
"""
TYPE HINTS
"""
def sum(x:int, y:int) -> int:
    result = x + y
    return result
"""
DEFAULT ARGUMENTS
"""
def greet(name="World"): #default name is "World"
    print("Hello, " + name + "!")

greet("Igor")
#"Hello, Igor!"
greet()
#"Hello, World"

"""
NAMED ARGUMENTS
"""
def greet(name="World",greeting="Hi"):
    print(greeting + ", " + name + "!")

greet(greeting="Hello",name="Igor")
#"Hello, Igor!"
greet(greeting="Hello")
#"Hello, World!"
""""""




"""
### Function Definition / Execution ###

Define a function called "bark()". When executed, "Woof" should get printed to the console.
Execute the function after its definition and run the program!
"""

# Write your solution here
def bark():
   print("Woof!")

bark()

"""
### Function with 1 Argument, additional logic ###

Write a program that asks the user to enter an animal. The program should respond with the corresponding animal sound.
Define a function called "make_sound(animal)". The function should use the given input to print the correct animal sound.
Add functionality for at least 3 animals and print the right sounds.
If the animal doesn't exists in the program, print "???".
Use a loop to repeatedly ask the user to enter another animal.
Make sure that upper- and lowercase letters both work when entering an animal.

Examples:
    Please enter an animal: >> dog
    Woof
    Please enter an animal: >> Cat
    Meow
    ...
"""

# Write your solution here

while True:
   animal = input("Please enter an animal: ")
   #option1
   animal = animal.lower()
   def make_sound(animal):
       if animal == "dog":
           print("woof")
       elif animal == "cat":
           print("meow")
       elif animal == "bear":
           print("growl")
       else:
           print("???")
   make_sound(animal)

#option2:
    # animal_input = ("Please enter an animal: ").lower()

#if we want to run the programm 5 times with while:
i = 0
while i < 4:
   animal_input = input("Please enter an animal: ")
   make_sound(animal_input)
   i += 1

#if we want to run the programm 5 times with for:
for i in range(0,5):
   animal_input = input("Please enter an animal: ")
   make_sound(animal_input)
   i += 1

"""
### Function with 2 Arguments ###

Write a function named print_many_times(text, times), which takes a string and an integer as arguments.
The integer argument specifies how many times the string argument should be printed out.

Example:
    print_many_times("Gimme Five!", 5)
    Gimme Five!
    Gimme Five!
    Gimme Five!
    Gimme Five!
    Gimme Five!

Additional Task:
Instead of "hard coding", let the user enter the text and the number of times to print it!
Ask the user repeatedly using a loop.
"""

# Write your solution here
while True:
    text = input("Please type in some text: ")
    times = int(input("How many times: "))
    def print_many_times(text: str, times: int):
        print(f"{text} \n" * times)
    print_many_times(text, times)

# # Z HODINY:
# def print_many_times(text: str, times: int):
#     #print(f"{text} \n" * times)
#     #print((text + "\n" * times))
#     for i in range(times):
#         print(text)
#     #namiesto for-loop:
#     i = 0
#     while i < 5:
#         print(text)
#         i += 1
# print_many_times("Gimme Five!", 5)

"""
### Return Values ###

Define a function named greatest_number, which takes three arguments. The function returns the greatest in value of the
three. Use the already defined function "print_greatest" and pass the return value of your function to it!

Example:
    return_value = greatest_number(3, 4, 1)
    print_greatest(return_value)
    The greatest number is 4!

Additional Task:
Add a type hint to the return value of the function!
"""

# Write your solution here
def greatest_number(a: int, b: int, c: int) -> int:
     if a > b and a > c:
         return a
     elif b > a and b > c:
         return b
     elif c > a and c > b:
         return c
     #if all three are equals it returns a
     else:
         return a

#this function takes in a single argument
def print_greatest(number: int) -> int:
    print(f"The greatest number is {number}!")

print_greatest(greatest_number(2,1,9))

# ???
#assigns the result of calling greatest_number(6, 2, 8) to the variable return_value.
#return_value = greatest_number(6,2,8)
#print_many_times(return_value) ???


"""
### Type Hints ###

Refactor your programs from above and add type hints to all function arguments and return values (if available)!
"""

# No code here, refactor the programs above!

"""
### Named arguments ###

Define a function named super_print which takes two arguments, a string and a boolean value.
If the boolean value is false, print the text as it was. If its True, print it in all upper case.
Use named arguments to use a different order of the arguments. First, use the string as first argument. For the second
call, use the boolean value as the first argument. Also, make use of type hints for the function arguments.

Example Outputs:
    HELLO WORLD
    hello world
"""

# Write your solution here
def super_print(text: str, uppercase: bool) -> None:
    """
        Prints the given text either as-is or in all uppercase, based on the value of the 'uppercase' argument.

        Args:
            text (str): The input text.
            uppercase (bool): If True, print the text in uppercase; otherwise, print it as-is.
        """
    if uppercase != False:
        print(text.upper())
    else:
        print(text)
#do zatvorky musim zadat oba argumenty, v tomto pripade user nezadava input
super_print('martina', False)
super_print('martina', True)
#
# ###
# # Example usage:
# super_print("hello world", uppercase=False)  # Output: hello world
# super_print("hello world", uppercase=True)   # Output: HELLO WORLD
#
# # First call with string as first argument
# super_print(text="hello world", uppercase=False)
# # Second call with boolean value as first argument - if we want to mix the arguments, we need to use the argument names as well
# super_print(uppercase=True, text="hello world")
# ###

"""
### Default Values ###

Define a simple function greet() that takes one argument "name". The function should print a greeting for the entered
name. Ask the user for his/her name and execute the greet function, passing the name as an argument.
If nothing was entered, use a default value for the name to greet "Unknown".

Hint: An empty string is still a value you can pass, be careful :-)

Example:
    Please enter your name: >> René
    Hello René!
    Please enter your name: >>
    Hello Unknown!
"""

# Write your solution here

# # NOT WORKING !!!!
# def greet(name="Unknown"):
#     print(f"Hello, {name}!")
# input_name = input("Please enter your name: ")
# greet(input_name)
#
#
# #WITH CONDITIONALS
input_name = input("Please enter your name: ")
def greet(input_name):
    if input_name == ():
        print("Hello, Unknown!")
    else:
        print(f"Hello, {input_name}!")
greet(input_name)

"""
INTRO to Python excercises

Fibonacci sequence
"""
# def fib(n):
#     """This is documentation string for function. It'll be available by fib.__doc__()
#     Return a list containing the Fibonacci series up to n."""
#     result = []
#     a = 1
#     b = 1 # Assign an initial value to the b variable
#     while a < n:
#         result.append(a)
#         tmp_var = b
#         b = a + b # Update the b variable with a sum
#         a = tmp_var # Restore the old value of the b variable to the a variable from the temp
#     return result# Here we need to return the result to the caller

"""
Printing out table with different symbols
"""
# def print_table(height, length=3, symbol='++++'):
#     for y in range(height):
#         for x in range(length):
#             print(f'|{symbol}', end='')
#         print('|\n')
#
# print_table(length=5, height=5, symbol='____') #the order of arguments doesn‘t matter

"""
ASSIGNMENT - GROUP A

Reversed word
Write a function named reverse_word which accepts one string argument (word) and returns the reversed word. Besides
reversing the word, the first letter of the reversed word should be written capitalized, all other letters should
be lower case letters.

Make use of type hints when declaring the function.

Example calls of function with corresponding return values:
reverse_word („hello“) -> „Olleh“
reverse_word („WORLD“) -> „Dlrow“
reverse_word („leOn“) -> „Noel“

"""

def reverse_word(word: str) -> None: #The -> None indicates that this function does not return any value; instead, it prints the result.
    reversed_word = "" # the empty string will be used to build the reversed version of the input word
    for i in range(len(word) - 1, -1, -1): # This line starts a for loop that will iterate over the indices of the input word in reverse order.
        # len(word) - 1 is the last index of the string (since indices start at 0).
        # -1 is the stop value for the range, which is one less than the start index, allowing the loop to run until the first character of the string.
        # -1 is the step value, which means the loop will decrease the index by 1 in each iteration, moving backwards through the string.
        reversed_word += word[i] # Inside the loop, we add the current character to the front of reversed_word, effectively reversing the string as the loop progresses.
    print(reversed_word[0].upper() + reversed_word[1:].lower())

reverse_word(word='martina')
reverse_word("MarTina")
reverse_word ("hello")
reverse_word ("WORLD")
reverse_word ("leOn")


#TOMMY AFTER ASSIGNMENT: ?????
def reverse_word(word: str):
    reversed_word = ""
    for i in range(0, len(word), -1):
        reversed_word += word[i]
    #print(reversed_word)

    return reversed_word[0].upper() + reversed_word[1::]
    # the longer and not necessary form is:
    # return reversed_word[0].upper() + reversed_word[1:len(reversed_word):1]


# solution with LISTS KNOWLEDGE:
def reverse_word(word: str) -> None:
    print(word[::-1].capitalize())

reverse_word(word='martina')
reverse_word("MarTina")
reverse_word ("hello")
reverse_word ("WORLD")
reverse_word ("leOn")

"""
SIMPLE CALCULATOR
Write a function named calculate which gets the following arguments passed: 2 integer numbers (operands) and a specific string operator (f.e. -, +, /, *). The function then executes the corresponding operation and prints result to the console.

In the case of division by 0, „Division by 0 is not allowed.“ is printed on the console. If an invalid operator is passed, „Invalid operator.“ is printed.

Make use of type hints when declaring the function.

Example calls of functino with corresponding console output:
calculate (3, 4, „+“) >> 7
calculate (2, 8, „-„) >> -6
calculate (10, 0 „/") >> Division by 0 is not allowed.
"""
def calculate(x: int, y: int, z: str) -> int:
    if z == "+":
        return x + y
    elif z == "-":
        return x - y
    elif z == "*":
        return x * y
    elif z == "/":
        if y == 0:
            print("Division by 0 is not allowed.")
        else:
            return x / y
    else:
        print("Invalid operator.")

calculate(1,4,'+')

"""
ASSIGNMENT - GROUP B

PALINDROMES
Write a function called is_palindrome that takes a string as parameter input and returns Boolean value True if the
string is a palindrome, and False otherwise. A palindrome is a word or phrase, that reads the same forward and backward,
ignoring spaces and capitalization.

Make use of hints when declaring the function

Hint: To replace a specific character in a string you can use replace method, eg.: „hello“.replace(„e“, „lo“) will
replace all occurrences of „e“ with „o“ -> „hollo“

Example calls of function with corresponding return values:
is_palindrome(„taco cat“) -> True
is_palindrome(„Step on no pets.“) -> True
is_palindrome(„Never odd or even“) -> True
is_palindrome(„Me no palindrome“) -> False
"""

#SOLUTION COPILOT:
def is_palindrome(s:str) -> bool:
    s.replace(" ", "").lower()

    # Remove spaces and convert to lowercase
    cleaned_s = s.replace(" ", "").lower()

    # Initialize pointers for the start and end of the string
    start = 0
    end = len(cleaned_s) - 1

    # Loop until the middle of the string is reached
    while start <= end:
        if cleaned_s[start] != cleaned_s[end]:
            return False
        start += 1
        end -= 1

    return True

# Example calls
print(is_palindrome("taco cat"))  # Output: True
print(is_palindrome("Step on no pets."))  # Output: True
print(is_palindrome("Never odd or even"))  # Output: True
print(is_palindrome("Me no palindrome"))  # Output: False

"""
MULTIPLICATION TABLE

Write a function named print_multiplication_table which gets the following arguments passed: two integer values, 
first a certain number for which the multiplicatoin table shall be printed and secondly a number that specifies the numbers of rows.

Only numbers bigger than 0 are valid numbers. Print an error message if either the number or the rows are zero or negative.

Make use of type hints when declaring the function.

Example calls of function with corresponding console output:
print_multiplication_table(6, 3) >>
1 * 6 = 6
2 * 6 = 12
3 * 6 = 18

print_multiplication_table(10, 2) >>
1 * 10 = 10
2 * 10 = 20

print_multiplication_table(-10, 2) >>
Number and rows cannot be less than 1.

print_multiplication_table(0, 0) >>
Number and rows cannot be less than 1.
"""

def print_multiplication_table(number:int, rows:int) -> None:
    if number <= 0 or rows <= 0:
        print("Number and rows cannot be less than 1.")

    index = 1
    while index <= rows:
        print(f"{index} * {number} = {index * number}")
        index += 1

print_multiplication_table(6, 3)

"""
TOMMY TUTORIUM

"""
def secondSmallestNum(nums: list) -> int:
    smallest = min(nums)
    second_smallest = max(nums)
    for num in nums:
        if num < second_smallest and num > smallest:
        second_smallest = num

def secondSmallestNumV2(nums: list) -> int:
    copyNums = nums.copy()
    smallest = min(copyNums)
    smallest_count = copyNums.count(smallest)
    for i in range(smallest_count):
        copyNums.remove(smallest)
    return min(copyNums)