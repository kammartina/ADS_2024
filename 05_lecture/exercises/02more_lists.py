"""
Write a function named list_of_stars, which takes a list of integers as its argument.
The function should print out lines of star characters. The numbers in the list specify how many stars each line should contain.

For example, with the function call list_of_stars([3, 7, 1, 1, 2]) the following should be printed out:

    ***
    *******
    *
    *
    **

"""
# Provide your solution here
def list_of_stars(numbers: [int]): # the argument is a list of integers
    # This 'for' loop iterates over each integer in the list 'numbers'.
    for num in numbers: # For each integer 'num', it prints a line of stars ('*').
        print("*" * num)
#numbers = [2,5,8,1,4]
list_of_stars([2,5,8,1,4])

# UNNECESSARY THINGS in the code:
# # Using 'range()' when you have specific numbers in a list is unnecessary:
# numbers = [3, 7, 1, 1, 2]
# for i in range(0, len(numbers)):
#     print('*' * numbers[i])
#
# # Directly iterating over the list is more straightforward and Pythonic:
# for num in numbers:
#     print('*' * num)


# if using NUMBERS from USER‘S INPUT:
def list_of_stars(numbers):
    for num in numbers:
        print('*' * num)
#Ask the user for a list of numbers, separated by spaces
user_input = input("Enter a list of numbers separated by spaces: ")
# Convert the input string into a list of integers
# [int(num) for num in user_input.split()] is a list comprehension that converts each substring into an integer,
# resulting in a list of integers. This list is stored in the variable numbers.
numbers = [int(num) for num in user_input.split()]
list_of_stars(numbers)

"""
Write a function named anagrams, which takes two strings as arguments.
The function returns True if the strings are anagrams of each other.
Two words are anagrams if they contain exactly the same characters.

Some examples of how the function should work:

    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False
"""
# Provide your solution here
def anagrams(str1:str, str2:str):
# Sort the characters of the strings and compare the sorted strings
    return sorted(str1) == sorted(str2)

print(anagrams("tame", "meta"))
print(anagrams("tame", "mate"))
print(anagrams("tame", "team"))
print(anagrams("tabby", "batty"))
print(anagrams("python", "java"))


# if TWO STRINGS contain the SAME LETTERS (need NOT to be anagrams) of each other:
# def compared_words(str1, str2):
#     # Remove spaces and lowercase the strings
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()
#
#     # Use a set to compare the unique characters in both strings
#     return set(str1) == set(str2)
#
# # Example usage:
# print(compared_words("triangle", "integral"))  # Output: True
# print(compared_words("hello", "world"))        # Output: False

"""
Write a function named sum_of_positives, which takes a list of integers as its argument.
The function returns the sum of the positive values in the list.

    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result) # prints The result is 9

"""
# Provide your solution here
def sum_of_positives(numbers):
    total = 0 #the variable 'total' will keep track of the sum of positive numbers.
    for number in numbers: #A for loop is used to iterate over each element in the numbers list.
        if number > 0:
            total += number
    return total

my_list = [1, -2, 3, -4, 5]
result = sum_of_positives(my_list)
print("The result is", result)

"""
Write a function named even_numbers, which takes a list of integers as an argument.
The function returns a new list containing the even numbers from the original list.

    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)

    Prints:
        original [1, 2, 3, 4, 5]
        new [2, 4]
"""
# Provide your solution here
def even_numbers(my_list):
    evens = [] # Create an empty list to hold the even numbers
    for numbers in my_list: # for loop to loop over the numbers of my_list
        if numbers % 2 == 0: # Check if the number is even
            evens.append(numbers) # Add the even number to the list
    return evens # After the loop, we return the evens list, which contains all the even numbers from the original list.

my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)
print("original", my_list)
print("new", new_list)
#
#
# # alebo zjednodusene - LIST COMPREHENSION:
# The list comprehension iterates over each number in the numbers list and includes it in the new list if
# number % 2 == 0 (which checks if the number is even). The resulting list contains only the even numbers.
def even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]

# Example usage:
my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)
print("original", my_list)
print("new", new_list)

"""
Write a function named list_sum which takes two lists of integers as arguments.
The function returns a new list which contains the sums of the items at each index in the two original lists.
You may assume both lists have the same number of items.

An example of the function at work:

    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]
"""
# Provide your solution here
def list_sum(a: [int],b: [int]):
    result_list = []
    #The range(len(a)) generates a sequence of numbers, which serves as the indices for the lists.
    for index in range(len(a)): # ??? preco iba "a" v zatvorke ???
        #Inside the loop, the elements at the current index i from both list1 and list2 are added together using the + operator.
        result_list.append(a[index] + b[index])
    return result_list

a = [1, 2, 3]
b = [7, 8, 9]
print(list_sum(a, b))

"""
ASSIGNMENT - GROUP A

UPPER AND LOWER
Write a function count_upper_lower that accepts a string as input parameter (method argument) and calculates the
number of upper case letters and lower case letters of the provided string.

Afterwards, the calculated letters are printed to the console - the function does not return a value.

Hint: Two string methods that might prove useful are my_string.isupper() and my_string.islower()
"m".isupper() -> False
"m".islower() -> True
"M".isupper() -> True
"M".islower() -> False

Examples show printed values for a given string:
count_upper_lower("Simon says: Use 'print' in Python, to display information to the user or console.")

>> No. of Upper case characters: 3
>> No. of Lower case characters: 60

"""

def count_upper_lower(my_string:str) -> int:
    count_lower = 0
    count_upper = 0

    for character in my_string:
        count_lower = sum(1 for character in my_string if character.islower())
        count_upper = sum(1 for character in my_string if character.isupper())
        #if character in my_string.isupper():
        #    count_lower += 1
        #
        #if character in my_string.isupper():
        #    count_upper += 1

    print(f"No. of Upper case characters: {count_upper}")
    print(f"No. of Lower case characters: {count_lower}")

count_upper_lower("Martina is NervouS.")

"""
CHECK 33
Write a function has_33 that accepts a list of integers as input parameter (method arguments) and returns True if the list contains a 3 next to a 3 somewhere - if not False.

Inside "_main_" block below, call your function at least 3 times with different input parameters.
Save the Boolean value in variables and print them to the console.

Hint: List can be passed to function the same way we did with primitive types (see examples below).

Examples show the return values (not print!) of the function with different lists as input:
has_33([1,3,3]) -> True
has_33([1,3,1,3]) -> False
has_33([3,1,3]) -> False
"""

def has_33(nums) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# Examples
print(has_33([1, 3, 3]))  # -> True
print(has_33([1, 3, 1, 3]))  # -> False
print(has_33([3, 1, 3]))  # -> False

"""
ASSIGNMENT - GROUP B

BLACKJACK
Write a function calculate_score that accepts three integers between 1 and 11 as input parameters
(you can assume that only valid integers are passed to it).

The function returns a value based on the following rules:
- if their sum is less than or equal to 21, return their sum.
- if their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
    - finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
    - else return their adjusted sum

Following examples show the return values (not print!) of the function with different integers as input:
calculate_score(9, 9, 9) - BUST
calculate_score(2, 8, 11) - 21
calculate_score(3, 8, 11) - 12
calculate_score(11, 11, 11) -> BUST

"""
# Write the solution here:
def calculate_score(x:int, y:int, z:int) -> int:
    total_sum = x + y + z

    if total_sum <= 21: # Check if the sum is less than or equal to 21
        print(total_sum)

    elif total_sum > 21 and 11 in (x, y, z): # If the sum exceeds 21 and there's an eleven
        total_sum -= 10
        if total_sum > 21: # Return 'BUST' if the sum still exceeds 21 after adjustment
            print("BUST")
        else: # Else return the adjusted sum
            print(total_sum)

    else: # If the sum exceeds 21 and there's no eleven
        print("BUST")

calculate_score(9, 9, 9)
calculate_score(2, 8, 11)
calculate_score(3, 8, 11)
calculate_score(11, 11, 11)

"""
EVEN NUMBERS

Write a function even_positive_numbers that accepts a list as input parameter (method arguments)
and returns a new list containing only the positive(>= 0) even numbers from the given list.

Inside "_main_" block below, call your function at least 3 times with different input parameters.
Save the returned lists in variables and print them to the console.

Hint: Lists can be passed to function the same way we did with primitive types (see examples
below).

Following examples show the return values (not print!) of the function with different lists as
input:
even_positive_numbers([1, 2, 3]) -> [2]
even_positive_numbers([10, 22, 31, 24, 35, 36]) -> [10, 22, 24, 36]
even_positive_numbers([-10, -22, 31, 24, 35, 36]) -> [24, 36]

"""
# Write the solution here:
def even_positive_numbers(my_list: [int]) -> [int]:
    evens = []
    for numbers in my_list: # for loop to loop over the numbers of my_list
        if numbers % 2 == 0: # Check if the number is even
            evens.append(numbers) # Add the even number to the list
    return evens

even_positive_numbers([1, 2, 3])
even_positive_numbers([10, 22, 31, 24, 35, 36])
even_positive_numbers([-10, -22, 31, 24, 35, 36])



"""
SUDOKU SOLVER in Python:
1. Understand the Sudoku Puzzle: A standard Sudoku puzzle consists of a 9x9 grid divided into 9 smaller 3x3 boxes.
The goal is to fill the grid so that each row, column, and 3x3 box contains all of the digits from 1 to 9.
2. Represent the Puzzle in Python: Use a two-dimensional list (list of lists) to represent the Sudoku grid in Python.
Empty cells can be represented by zeros.
3. Find an Empty Space: Search the Sudoku grid to find an empty space (represented by 0 or another placeholder).
4. Attempt to Place Digits: Try placing digits 1 through 9 in that empty space.
5. Check Validity: Check if the current digit placement follows the Sudoku rules:
    No duplicate digits in the current row.
    No duplicate digits in the current column.
    No duplicate digits in the current 3x3 subgrid.
6. Recursive Backtracking:
    If the digit is valid, recursively attempt to fill the next empty space using the same algorithm.
    If the digit leads to no valid placement down the line (dead end), backtrack by replacing the digit with the placeholder again and try the next digit.
7. Solution Found or Not Possible:
    If all empty spaces are filled validly, a solution is found.
    If no digits are valid for an empty space, the Sudoku puzzle is unsolvable with the current placements, indicating backtracking is needed.
8. Repeat: Continue this process until the entire grid is filled.
9. Test Your Solver: Test your program with different Sudoku puzzles to ensure it works correctly.
Remember, the key to solving Sudoku with a program is the backtracking algorithm, which tries all possible numbers in
an empty cell until the puzzle is solved or it backtracks to try a different number.

"""

# def is_valid(board, row, col, num):
#     # Check if the number is not repeated in the current row, column, and 3x3 subgrid
#     for x in range(9):
#         if board[row][x] == num or board[x][col] == num:
#             return False
#     start_row, start_col = 3 * (row // 3), 3 * (col // 3)
#     for i in range(3):
#         for j in range(3):
#             if board[i + start_row][j + start_col] == num:
#                 return False
#     return True
#
# def solve_sudoku(board):
#     empty = find_empty_location(board)
#     if not empty:
#         return True  # No more empty spaces, puzzle solved
#     row, col = empty
#
#     for num in range(1, 10):
#         if is_valid(board, row, col, num):
#             board[row][col] = num
#             if solve_sudoku(board):
#                 return True
#             board[row][col] = 0  # Backtrack
#     return False
#
# def find_empty_location(board):
#     for i in range(9):
#         for j in range(9):
#             if board[i][j] == 0:
#                 return (i, j)
#     return None
#
# def print_board(board):
#     for row in board:
#         print(" ".join(str(num) for num in row))
#
#
# sudoku_board = [
# [0, 7, 0, 0, 0, 5, 0, 0, 0],
# [0, 0, 0, 9, 0, 8, 0, 6, 0],
# [0, 0, 8, 3, 0, 0, 0, 1, 0],
# [0, 2, 0, 8, 0, 0, 0, 3, 4],
# [0, 8, 0, 0, 0, 0, 0, 5, 0],
# [0, 1, 0, 6, 0, 7, 0, 0, 0],
# [9, 0, 2, 7, 0, 0, 5, 0, 0],
# [5, 4, 0, 0, 0, 0, 0, 2, 0],
# [0, 0, 0, 0, 6, 0, 0, 0, 0]
# ]
#
# if solve_sudoku(sudoku_board):
#     print_board(sudoku_board)
# else:
#     print("No solution exists")