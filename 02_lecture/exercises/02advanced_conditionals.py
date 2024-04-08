"""
Write a program which asks for two integer numbers.
The program should then print out whichever is greater.
If the numbers are equal, the program should print a different message.
Examples:
    Please type in the first number: >> 5
    Please type in another number: >> 3
    The greater number was: 5

    Please type in the first number: >> 5
    Please type in another number: >> 8
    The greater number was: 8

    Please type in the first number: >> 5
    Please type in another number: >> 5
    The numbers are equal!

"""
# Write your solution here
#input1 = int(input("Please type in the first number: "))
#input2 = int(input("Please type in the second number: "))
#if input1 == input2:
#    print(" The numbers are equal!")
#elif input1 > input2:
#    print(f"The greater number was {input1}")
#else:
#    print (f"The greater number was {input2}")
"""
Python comparison operators can also be used on strings. 
String a is smaller than string b if it comes alphabetically before b. Notice however that the comparison is only reliable if
- the characters compared are of the same case, i.e. both UPPERCASE or both lowercase
- only the standard English alphabet of a to z, or A to Z, is used.

Write a program which asks the user for two words. The program should then print out whichever of the two comes alphabetically last.

You can assume all words will be typed in lowercase entirely.

Examples:
Please type in the 1st word: >> car
Please type in the 2nd word: >> scooter
scooter comes alphabetically last.

Please type in the 1st word: >> zorro
Please type in the 2nd word: >> batman
zorro comes alphabetically last.

Please type in the 1st word: >> python
Please type in the 2nd word: >> python
You gave the same word twice.

"""
# Write your solution here
#word1 = input("Please type in the 1st word: ")
#word2 = input("Please type in the 2nd word: ")
#if word1 < word2:
#    print(f"The word that comes alphabetically last is: {word2}")
#elif word1 > word2:
#    print (f"The word that comes alphabetically last is: {word1}")
#else:
#    print("You gave the same word twice.")

"""
Write a program which asks for the user's name. 
If the name is Huey, Dewey or Louie, the program should recognise the user as one of Donald Duck's nephews.
In a similar fashion, if the name is Morty or Ferdie, the program should recognise the user as one of Mickey Mouse's nephews.

Examples:
    Please type in your name: >> Morty
    I think you might be one of Mickey Mouse's nephews.
    
    Please type in your name: >> Huey
    I think you might be one of Donald Duck's nephews.
    
    Please type in your name: >> Ken
    You're not a nephew of any character I know of.
"""
# Write your solution here
#username = input("What is your user‘s name? ")
#if username in ["Huey", "Dewey", "Louie"]:
#    print("I think you might be one of Donald Duck's nephews.")
#elif username in ["Morty", "Ferdie"]:
#    print("I think you might be one of Mickey Mouse's nephews.")
#else:
#    print("You're not a nephew of any character I know of.")

#Solution2:
#username = input("What is your user‘s name? ")
#if username == "Huey" or "Dewey" or "Louie":
#    print("I think you might be one of Donald Duck's nephews.")
#elif username == "Morty" or "Ferdie":
#    print("I think you might be one of Mickey Mouse's nephews.")
#else:
#    print("You're not a nephew of any character I know of.")
"""
FizzBuzz
Write a program which asks the user for an integer number. 
If the number is divisible by three, the program should print out Fizz. 
If the number is divisible by five, the program should print out Buzz. 
If the number is divisible by both three and five, the program should print out FizzBuzz.

Examples:
    Number: >> 9
    Fizz
    
    Number: >> 7
    
    Number: >> 20
    Buzz
    
    Number: >> 45
    FizzBuzz
"""
# Write your solution here
#number = int(input("Please type in an integer number: "))
#if (number % 3 == 0) and (number % 5 == 0):
#    print("FizzBuzz")
#elif number % 3 == 0:
#    print("Fizz")
#elif number % 5 == 0:
#    print("Buzz")
#else:
#    print("The number given ist‘t dividable by 3 and/or 5.")
#The % operator is key here; it returns the remainder of the division of
# the number by 3 or 5. If the remainder is 0, it means the number is divisible by that divisor.
"""
LeapYear
Generally, any year that is divisible by four is a leap year. 
However, if the year is additionally divisible by 100, it is a leap year only if it also divisible by 400.

Write a program which asks the user for a year, and then prints out whether that year is a leap year or not.

Examples:
    Please type in a year: >> 2011
    That year is not a leap year.
    
    Please type in a year: >> 2020
    That year is a leap year.
    
    Please type in a year: >> 1800
    That year is not a leap year.
"""
# Write your solution here
year = int(input("Please type in a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("That year is a leap year.")
else:
   print("That is not a leap year.")
#If the year is divisible by 4 but not by 100, it is a leap year.
#If the year is divisible by 100, it must also be divisible by 400 to be a leap year.