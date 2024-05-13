"""
MULTIPLYING STRINGS
"""
n = 5
row = "*"
while n > 0:
    print(" " * n + row)
    row += "**"
    n -= 1
"""
IN-operator #results in Boolean value

FIND method
my_string.find("xem")

"""
"""
FOR-loop

name = "LEON"
for character in name:
    print(character)

# L
# E
# O
# N

#FOR every CHARACTER in the string NAME
#PRINT the CHARACTER to the console

"""
RANGE function
-> to iterate through a string using its indices
-> returns a sequence of numbers from start (first parameter) to stop (second parameter)

alphabet = "ABCDEF..."
for index in range(0,len(alphabet)):
    print(alphabet[index])

# A
# B
# C
# D
# E
# F
# .
# .
# .<

"""
STRING METHODS

str.capitalize() => first character capitalized, others in lowercase
capitalized = my_string.capitalize()

str.lower() => any characters in uppercase to lowercase -> all in lowercase
lowered = my_string.lower()

str. upper() => any characters in lowercase to uppercase -> all in uppercase
upper_case = my_string.upper()

str.replace(old, new [count]) => "old" replaced by "new"; if the count argument is given, all count number of occurences are replaced
replaced = my_string.replace("hello", "hi")

str.strip() => removes leading and trailing whitespace from a string
stripped = my_string.strip()

split(separator) => splits a string into a list of substrings based on a specified separator
splitted = my_string.split(", ")

"""

"""
Write a program which asks the user for a string and an amount.
The program then prints out the string as many times as specified by the amount.
The printout should all be on one line, with no extra spaces or symbols added.

Example:
    Please type in a string: >> hey
    Please type in an amount: >> 4
    heyheyheyhey
"""
# Write your solution here
my_string = input("Please type in a string: ")
my_amount = input("Please type in an amount: ")
multiprint = str(my_string) * int(my_amount)
print(multiprint)

"""
Write a program which asks the user for two strings and then prints out whichever is the longer of the two - 
that is, whichever has the more characters. If the strings are of equal length, the program 
should print out "The strings are equally long".

Examples:

    Please type in string 1: >> hello
    Please type in string 2: >> world
    The strings are equally long
    
    Please type in string 1: >> hey
    Please type in string 2: >> world
    world is longer
"""
# Write your solution here

my_string1 = input("Please type in string 1: ")
my_string2 = input("Please type in string 2: ")

if len(my_string1) > len(my_string2):
   print(f"The longer string is: {my_string1}")
elif len(my_string1) < len(my_string2):
   print(f"The longer string is: {my_string2}")
else:
   print("The strings are equally long.")

"""
Write a program which asks the user for a string. The program then prints out the input string in reversed order, 
from end to beginning. Each character should be on a separate line.
Try to solve this example in 2 ways:
    * once using positive indeces
    * once using negative indeces
"""
# # String in normal order using positive indices:
my_string = input("Please type in a string: ")
for character in my_string:
    print(character)


# # REVERSED using POSITIVE indices:
my_string = input("Please type in a string: ")
length = len(my_string)
# using positive indices, so index starts with 0
i = 0
#the FOR-loop meaning - for every character in the string my_string print the character to the console
# Use a for loop with positive indices to print each character in reverse order
#Inside the loop, length - 1 - i is used to calculate the index of the character to be printed. Since i starts
# at 0 and increases, length - 1 - i starts at length - 1 (the last character’s index) and decreases to 0 (the
# first character’s index).
for i in range (length):
    print(my_string[length -1 - i])


# # String in normal order using negative indices ??:
# my_string = input("Please type in a string: ")
# i = -1
# for character in my_string:
#     print(character)


# # REVERSED using NEGATIVE indices:
my_string = input("Please type in a string: ")
# using negative indices, so index starts with -1
# we don‘t need reversing because it‘s already reversed
i = -1
length = len(my_string)
#The loop runs from -1 (the last character’s index) to -length (the first character’s index), stepping backwards by 1.
for i in range (-1, -length -1, -1):
    #my_string[i] accesses each character of the string using the negative index i
    print(my_string[i])

"""
Write a program which asks the user for a string. 
The program then prints out a message based on whether the second character and the second to last character 
are the same or not. See the examples below.

Examples:
    Please type in a string: >> python
    The second and the second to last characters are different
    
    Please type in a string: >> pascal
    The second and the second to last characters are a
"""
# Write your solution here

my_string = input("Please type in a string: ")

if my_string[1] != my_string [-2]:
   print("The second and the second to last characters are different.")
else:
   print(f"The second and the second to last characters are {my_string [1]}")

"""
Write a program which prints out a line of hash characters, the width of which is chosen by the user.

Examples:
    Width: >> 8
    ########
    
    Width: >> 2
    ##
"""
# Write your solution here

my_width = int(input("Width: "))
multiplication = str("#") * int(my_width)
print(multiplication)

"""
Modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.

Example:
    Width: >> 10
    Height: >> 3
    ##########
    ##########
    ##########
"""
# Write your solution here
my_width = int(input("Width: "))
my_height = int(input("Heigh: "))

for _ in range(my_height):
   print("#" * my_width)

#The underscore (_) is used as a THROWAWAY VARIABLE NAME, indicating that ITS VALUE IS NOT USED IN THE LOOP.

"""
Write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed. 
If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.

You may assume the input string is at most 20 characters long.

Examples:
    Please type in a string:hello
    ***************hello
    
    Please type in a string:helloworld
    **********helloworld 
"""
# Write your solution here
my_string = input("Please type in a string (max. 20 characters): ")

if len(my_string) == 20:
   print(my_string)
elif len(my_string) > 20:
   print(my_string[0:20])
else:
   asterisk_needed = 20 - len(my_string)
   padding = "*" * asterisk_needed
   print(padding + my_string)

#OidaOidaOidaOidaOidaO

"""
Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. 
The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.

Examples:
    Word: >> testing
    
    ******************************
    *          testing           *
    ******************************

    Word: >> python
    
    ******************************
    *           python           *
    ******************************
"""
# Write your solution here
my_string = input("Please type in a string (max. 28 characters): ")

if len(my_string) <= 28:
    #first row
    print("*" * 30)
#second row
#Calculate the number of spaces needed on each side of the word
    spaces_needed = (28 - len(my_string)) // 2
#Print the left border, word, and right border of the frame
    if len(my_string) % 2 != 0:
        spaces_needed += 1
        print("*" + " " * spaces_needed + my_string + " " * (spaces_needed - 1) + "*")
    else:
        print("*" + " " * spaces_needed + my_string + " " * spaces_needed + "*")
# If the length of the input string is odd, adjust the spaces

    # third row
    print("*" * 30)
else:
    print("The maximal length is 28 characters!")

"""
Write a program which asks the user to type in a string. 
The program then prints out all the substrings which begin with the first character, 
from the shortest to the longest. Have a look at the example below.

Example:
    Please type in a string: >> test
    t
    te
    tes
    test
"""
# Write your solution here
my_string = input("Please type in a string: ")
# Iterate over the input string
for i in range (0, len(my_string)):
   # Print substrings starting from the first character
   print(my_string[:i + 1])

#Solution which starts with every letter from my_string and adds letters...
# my_string = input("Please type in a string: ")
# for i in range (0, len(my_string)):
#    for j in range (i + 1, len(my_string) + 1):
#        print(my_string[i:j])
#Output:
# t
# te
# tes
# test
# e
# es
# est
# s
# st

"""
Write a program which asks the user to type in a string. 
The program then prints out all the substrings which end with the last character, from the shortest to the longest. 
Have a look at the example below.

Example:
    Please type in a string: >> test
    t
    st
    est
    test
"""
# Write your solution here (using negative indices)
my_string = input("Please type in a string: ")
i = -1
# The loop runs from -1 (the last character’s index) to -length (the first character’s index), stepping backwards by 1.
# MEANING:
#t[-1],e[-2],s[-3],t[-4]
#zaciatok je na pozicii -1; -len(my_string) znamena ze pokracujeme az na zaciatok slova;
#-len(my_string) -1 znamena ze na konci slova este o jeden index dalej aby sa vytlacilo aj cele slovo
#posledna -1 znamena ze for loop ma ist stale o jednu poziciu dalej (v tomto pripade uberat o jednu poziciu)
for i in range (-1, -len(my_string) -1, -1):
   # Print substrings starting from the first character do konca slova; v zapornych cislach!
   print(my_string[i:])



# # Solution with POSITIVE indices:
# my_string = input("Please type in a string: ")
# for i in range (0, len(my_string)):
#    # Print substrings starting from the first character
#    print(my_string[i:])

# Output:
# test
# est
# st
# t

"""
Write a program which asks the user to input a string. The program then prints out different messages if the string 
contains any of the vowels a, e or o.

You may assume the input will be in lowercase entirely. Have a look at the examples below.

    Please type in a string: >> hello there
    a not found
    e found
    o found
    
    Please type in a string: >> hiya
    a found
    e not found
    o not found
"""
# Write your solution here
my_string = input("Please type in a string: ")

if "a" in my_string:
   print("a found")
else:
   print("a not found")

if "e" in my_string:
   print("e found")
else:
   print("e not found")

if "o" in my_string:
   print("o found")
else:
   print("o not found")

"""
Write a program which asks the user to type in a string and a single character. The program then 
prints the first three character slice which begins with the character specified by the user. 
You may assume the input string is at least three characters long. The program must print out three characters, 
or else nothing.

Pay special attention to when there are less than two characters left in the string after the first occurrence of 
the character looked for. In that case nothing should be printed out, and there should not be any indexing errors 
when executing the program.

Examples:

    Please type in a word: >> mammoth
    Please type in a character: >> m
    mam
    
    Please type in a word: >> banana
    Please type in a character: >> n
    nan
    
    Please type in a word: >> python
    Please type in a character: >> n
"""
# Write your solution here
my_string1 = input("Please type in a string: ")
my_string2 = input("Please type in a single character: ")

# Find the first occurrence of the character + definujem index
index = my_string1.find(my_string2)
# Check if there are at least two characters after the found character
if index != -1 and index + 2 < len(my_string1):
   # Print the three character slice
   print(my_string1[index:index+3])
else:
   print("")

"""
Write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, 
the program should print out a message accordingly.

In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the 
substring aa is at index 2.

Examples:

    Please type in a string: >> abcabc
    Please type in a substring: >> ab
    The second occurrence of the substring is at index 3.
    
    Please type in a string: >> methodology
    Please type in a substring: >> o
    The second occurrence of the substring is at index 6.
    
    Please type in a string: >> aybabtu
    Please type in a substring: >> ba
    The substring does not occur twice in the string.
"""
# Write your solution here
my_string = input("Please type in a string: ")
my_substring = input("Please type in a substring: ")

# Find the first occurrence of the substring
first_index = my_string.find(my_substring)
#-> index sa zacina tam, kde sa najde ten substring, ktory user zadal na zaciatku

# If the first occurrence is found...
if first_index != -1:
    #then initialize the index for the second occurrence and , look for the second occurrence
    second_index = my_string.find(my_substring, first_index + len(my_substring))
    #->druhy index sa zacina od najdenia prveho indexu kdekolvek do konca slova
    #If the second occurrence is found...
    if second_index != -1:
        print(f"The second occurrence of the substring is at index {second_index}")
    #second occurrence not found:
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur in the string.")