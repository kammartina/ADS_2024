"""
Write a program that asks for a user's name and then prints it twice

    What is your name? >> Leon
    Leon
    Leon
"""
name = input("What is your name? ")
print(name)
print(name)

"""
 Write a program that asks for a user's name and then prints it out twice separated by exclamation marks

    What is your name? >> Leon
    !Leon!Leon!
"""
name = input("What is your name? ")
print("!",name,"!",name)

"""
Here is a program which should ask for three utterances and print them out, like so:

    The 1st part: >> hickory
    The 2nd part: >> dickory
    The 3rd part: >> dock
    hickory-dickory-dock!
"""

# Fix the code
part1 = input("The 1st part: ")
part2 = input("The 2st part: ")
part3 = input("The 3st part: ")
print(part1, "-", part2, "-", part3, "!")


"""
Write a program which prints out the following story. The user gives a name and a year, which should be inserted into the printout.

    Please type in a name: >> Mary
    Please type in a year: >> 1572
    
    Mary is a valiant knight, born in the year 1572. One morning Mary woke up to an awful racket: a dragon was approaching the village. Only Mary could save the village's residents.
"""
name1 = input("Please type in a name: ")
name2 = input("Please type in a year: ")
print(name1, "is a valiant knight, ", end="")
print("born in the year", name2,". ", end="")
print("One morning ",name1, "woke up to an awful racket: ", end="")
print("a dragon was approaching the village. ", end="")
print("Only ",name1, "could save the village's residents.")