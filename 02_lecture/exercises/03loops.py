"""
Write a program that prints out the message "hello world!" and then asks "shall we continue?"
until the user inputs "no". Then the program should print out "okay then" and finish.

Example:
    hello world!
    shall we continue? >> yes
    hello world!
    shall we continue? >> oui
    hello world!
    shall we continue? >> jawohl
    hello world!
    shall we continue? >> no
    okay then
"""
# Write your solution here
print("Hello world!")
while True:
 user_input = input("Shall we continue? ")
 if user_input == "no":
   print("Okay then, bye!")
   break

"""
Write a program which asks the user for integer numbers.

- If the number is below zero, the program should print out the message "invalid number".
- If the number is above zero, the program should print out the square root of the number using the Python sqrt function.
- In either case, the program should then ask for another number.
- If the user inputs the number zero, the program should stop asking for numbers and exit the loop.

To use the `sqrt` function in python add the following to the top of your file: 
    from math import sqrt
Then use it like:
    print(sqrt(9))
    
Example:
    Please type in a number: >> 16
    4.0
    Please type in a number: >> 4
    2.0
    Please type in a number: >> -3
    invalid number
    Please type in a number: >> 1
    1.0
    Please type in a number: >> 0
    Exiting...
"""
# Write your solution here
from math import sqrt
while True:
  user_input = int(input("Please type in a number: "))
  if user_input == 0:
    print("Exiting...")
    break
  elif user_input < 0:
    print("invalid number")
  else:
    print(sqrt(user_input))

#Solution2:
import math
while True:
 number = int(input("Please type in a number: "))
 if number < 0:
   print("Invalid number!")
 elif number > 0:
   square_root = math.sqrt(number)
   print(f"The square root of {number} is {square_root}")
 else:
   print("Exiting...")
   break
"""
This program should print out a countdown. However, the program doesn't quite work. Please fix it.
Hint: you can use the debugger of PyCharm to see how the program is executing.
"""
# Fix the code
#number = 5
#print("Countdown!")
#
#while True:
#  if number > 0:
#    print(number)
#    number = number - 1
#    continue
#  else:
#    break
#
#print("Now!")
###

print("Countdown!")
Initialize the number before the loop
number = 5
while number > 0:
 print(number)
  Decrement the number by 1
 number -= 1
print("Now!")

"""
Write a program which asks the user for a year, and prints out the next leap year.
If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year.

Examples:
    Year: >> 2023
    The next leap year after 2023 is 2024
    
    Year: >> 2024
    The next leap year after 2024 is 2028
"""
# Write your solution here
year = int(input("Year: "))

while True:
   year += 1
   if year % 4 == 0:
       #after the word "after" is not the year that the user entered, but the last leap year that we had and
       #and the next leap year will be calculated
       print(f"The next leap year after {year - 4} is {year}")
       break

"""
Please write a program which keeps asking the user for words. 
If the user types in end, the program should print out the story the words formed, and finish.

Example:
  Please type in a word: >> Once
  Please type in a word: >> upon
  Please type in a word: >> a
  Please type in a word: >> time
  Please type in a word: >> there
  Please type in a word: >> was
  Please type in a word: >> a
  Please type in a word: >> girl
  Please type in a word: >> end
  Once upon a time there was a girl
"""
# Write your solution here

#Initializes the "story" variable with a single space. This will be used to accumulate the words entered by the user.
#meaning: to accumulate, or add together, the words entered by the user with spaces in between
story = " "
#Starts an infinite loop. This loop will continue to run until it’s explicitly broken out of with the break statement.
while True:
 word = input("Please type in a word ("end" for exit): ")
 if word == "end":
   break
 story += word + " "
print(story)

# EXPLANATION: story += word + " "
#   "story" is the variable that holds the accumulated story so far.
#   "+=" is the in-place addition operator. It adds the right-hand side to the left-hand side and then assigns the
#     result back to the left-hand side. In the context of strings, it concatenates them.
#   "word" is the variable that holds the most recent word entered by the user.
#   " " This is a single space character as a string. It’s added after word to ensure that words are separated by spaces
#     in the story.

"""
Change the program above so that the loop ends also if the user types in the same word twice in a row.
"""
# Write your solution here

story = " "
#initialize last_word as an empty string (""), which will keep track of the last word entered
last_word = ""
while True:
  word = input("Please type in a word ("end" for exit): ")
  if word == "end" or word == last_word:
    break
  story += word + " "
  #we update last_word with the current word
  last_word = word
print(story)

"""
Please write a program which asks the user for integer numbers. 
The program should keep asking for numbers until the user types in 0.

After reading the numbers the program should 
  - print out how many numbers were typed in
  - the sum of numbers entered
  - the mean of numbers entered
  - the number of positive and negative numbers entered
  
Example output
  Numbers typed in 4
  The sum of the numbers is 34
  The mean of the numbers is 8.5
  Positive numbers 3
  Negative numbers 1
"""
# Write your solution here:

# Initialize variables
total_sum = 0
count_numbers = 0
count_positive = 0
count_negative = 0

while True:
  user_input = int(input("Please type in a number (0 for exit): "))
  if user_input == 0:
    break
  total_sum += user_input
  count_numbers += 1
  if user_input > 0:
    count_positive += 1
  elif user_input < 0:
    count_negative += 1

#dividing total_sum by count_numbers, but only if at least one number was entered (to avoid division by zero)
#meaning: total_sum divided by count_numbers, ale iba ak sa count_numbers nerovna nule, lebo inak bude vysledok tohto celeho nula
mean = total_sum // count_numbers if count_numbers != 0 else 0

print(f"The numbers typed in: {count_numbers}")
print(f"The sum of the number is {total_sum}")
print(f"The mean of the numbers is: {mean}")
print(f"Positive numbers: {count_positive}")
print(f"Negative numbers: {count_negative}")

"""
Largest Number

Write a program which asks the user for float numbers.
The program should keep asking for numbers until the user types in 0 or a negative number.
The program should then print the largest number.
If the first number entered is less than or equals to 0, the program should quit and print "no number entered".

DO NOT USE LISTS TO SOLVE THIS EXERCISE!

Examples:
  Number 1: >> 3
  Number 2: >> 4.67
  Number 3: >> 120.5
  Number 4: >> 70
  Number 5: >> 0
  The largest number is 120.5
  
  Number 1: >> -1.11
  No number entered.
"""
# Write your solution here
counter = 0
#largest_number is set to -1, which acts as a FLAG VALUE indicating that NO NUMBERS HAVE BEEN ENTERED YET
largest_number = -1

while True:
  user_input = float(input(f"Number {counter} (0 for exit): "))
  if counter == 1 and user_input <= 0:
    print("no number entered")
    break

  if user_input == 0:
    break

  #For each positive number entered, the program checks if it’s larger than the current largest_number.
  #If it is, largest_number is updated to this new value.
  if user_input > largest_number or largest_number == -1:
    largest_number = user_input

  counter += 1

# If a largest number has been found, print it
if largest_number != -1:
  print(f"The largest number is: {largest_number}")

"""
Write a program that reads in an integer number (number of lines) and generates the subsequent output using 
two loops on the console (see below). 
If the input of numbers is smaller or equal to 0 an error message should be printed.

Examples:
  n: >> 4
  1
  2 3
  4 5 6
  7 8 9 10
  
  n: >> -1
  Invalid number!
"""
# Write your solution here
n = int(input("n: >> "))
if n <= 0:
  print("Invalid number!")
else:
  #We initialize two more variables: "num" (to keep track of the current number)
  # and "line" (to keep track of the current line).
  num = 1
  line = 1
  #We use a while loop to iterate through each line. The loop continues until line is less than or equal to n.
  while line <= n:
    #Inside the outer loop, we use another while loop to print the numbers in each line.
    #The inner loop continues until count is less than line.
    count = 0
    while count < line:
      #We print the current value of num.
      #Increment num by 1.
      #Increment count by 1.
      print(num, end=' ')
      num += 1
      count += 1
    # New line after each row
    print()
    #we increment line by 1 to move to the next line and repeat the process until all lines are printed
    line += 1

"""
Write a program that uses loops to create a pyramid of stars '*' on the console. 
The pyramid should have exactly 6 rows.
Example:
       *
      ***
     *****
    *******
   *********
  ***********
"""
# Write your solution here
n = 6
row = "*"
while n > 0:
  print(" " * n + row)
  row += "**"
  n -= 1

"""
Write a program to calculate the average grade. The console reads in grades between 1 and 5 
until the number 0 is entered. If an invalid grade is entered, an error message is displayed, 
the grade is not counted and the prompt progresses. It is assumed that only integers are entered. 
At the end of the input, the grade average and the number of negatives (grade = 5) are output.

Example:
  Mark 1: >> 5
  Mark 2: >> 3
  Mark 3: >> 10
  Invalid mark!
  Mark 3: >> 1
  Mark 4: >> 5
  Mark 5: >> 0
  Average: 3.50
  Negative marks: 2
"""
# Write your solution here
counter = 1
total_sum = 0
count_numbers = 0
count_negative = 0

while counter <= 5:
  user_input = int(input(f"Mark {counter}: "))
  if user_input < 0 or user_input > 5:
    print("Invalid mark!")
    continue
  else:
    total_sum += user_input
    count_numbers += 1

  if user_input == 5:
    count_negative += 1

  counter += 1

average = total_sum // count_numbers
print(f"Average: {average}")
print(f"Negative marks: {count_negative}")

"""
Assignment Group B:
"""
#TASK 02
#Write a program that repeatedly asks users to enter three numbers (integer) and outputs whether
#the numbers entered are in ascending order, descending order, or in neither.

#The program then prints "ascending", "descending" or "no specific order".

#Additionally, if the entered numbers are not ordered ascending or descending, it checks if all
#numbers are even (divisible by 2) or odd.

#n1 = int(input("The first number is: "))
#n2 = int(input("The second number is: "))
#n3 = int(input("The third number is: "))

#if n1 < n2 < n3:
#  print("The numbers are in ascending order.")
#elif n1 > n2 > n3:
#  print("The numbers are in descending order.")
#else:
#   print("The numbers are in no specific order.")
#   if n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0:
#     print("The numbers are even.")
#   elif n1 % 2 != 0 and n2 % 2 != 0 and n3 % 2 != 0:
#     print("The numbers are odd.")
#   else:
#     print("The numbers may be even or odd.")

""""""
#TASK 01
#Write a program that reads in two integers n1 and n2 from the user and outputs the sum of all
#integers from n1 to n2 (inclusively).
#If n1 or n2 (or both) are smaller or equal to 0, the program should print a corresponding message. If
#both numbers are greater than 0, but n2 is less than n1, an error message should also be printed.

#start = int(input("The first number is: "))
#end = int(input("Put in a higher number: "))
#if start > end:
#  print("The second number needs to be higher than the first number.")
#else:
#  if start <= 0 or end <= 0:
#    print("Either number can‘t be negative.")
#  else:
#    sum = [i for i in range(start, end)] #list function
#    print(sum)

"""
Assignment Group A
"""
"""
#Task 01 – Cashbox
Write a program that reads in an amount to be paid (int) and an amount received (int) from user.
The program calculates the change, prints it, and terminates.
If the amount received is too small, a corresponding error message is printed, and the user input is
repeated.
If the amount to be paid and/or the amount received is less than 0, the input is incorrect. In that
case, the program should also print a message and repeat the user input.
"""

to_be_paid = int(input("To pay: "))
amount_received = int(input("Received: "))
change = to_be_paid - amount_received

while True:
 if amount_received < 0:
   print("Negative payment is invalid!")
   to_be_paid = int(input("To pay: "))
   amount_received = int(input("Received: "))
 else:
   if change == 0:
     print("Thank you!")
     break
   elif amount_received > to_be_paid:
     print(f"Thank you! Your change is: {amount_received - to_be_paid}")
     break
   elif amount_received < to_be_paid:
     print("You did not pay enough. Please, pay more.")
     to_be_paid = int(input("To pay: "))
     amount_received = int(input("Received: "))



"""
Excercises Loops (YouTube)
"""
#Write a program to display the even number between 1 and 10. After that print the messege
#how many even numbers were printed.

#to count the numbers we need a separate variable
count = 0

for number in range(1, 10):
 if number % 2 == 0:
   #every time we find an even number we need to increment
   count += 1
   print(number)

print(f"We have {count} even numbers.")
