"""
Exercises "Lists"
"""
# # REMOVE - content number; only the first occurrence:
# numbers = [1,2,3,4,5,2,4]
# numbers.remove(2)
# print(numbers)
#
# # REMOVE - content number; in the whole list - using loop:
# def removing_all(numbers):
#     while 2 in numbers:
#         numbers.remove(2)
# removing_all(numbers)
# print(numbers)
#
# # POP - removes index; just one index:
# numbers = [1,2,3,4,5,2,4]
# numbers.pop(2)
# print(numbers)
#
# # POP - removes and returns index; just one index:
# numbers = [1,2,3,4,5,2,4]
# removed = numbers.pop(2)
# print(removed) #prints removed number
# print(numbers) #prints the list without the removed number
#
# # SORT:
# numbers = [1,2,3,4,5,2,4]
# numbers.sort()
# print(numbers)
#
# # SORTED:
# numbers = [1,2,3,4,5,2,4]
# print(sorted(numbers))
#
# # MIN, MAX, SUM:
# numbers = [1,2,3,4,5,2,4]
# print("Sum:", sum(numbers))
#

"""
### List Initialization and Accessing Items ###

Create a list named "colors" containing at least five different colors as strings. 
Print the third color in the list.
"""

# Write your solution here
colors = ['red', 'blue', 'green', 'violet', 'yellow']
print(colors[2])

"""
### List Mutability ###

Initialize a list of numbers from 1 to 5. Change the second number in the list to 10.
Print the modified list.
"""

# Write your solution here
numbers = [1,2,3,4,5]
numbers[1] = 10
print(numbers)


"""
### Append and Insert Method ###

Create an empty list named "pets". Use the append method to add "dog", "cat", and "bird" to the list.
Then use the insert method to add "lizard" at the second position in the list.
Print the updated list.
"""

# Write your solution here
pets = []
pets.append("dog")
pets.append("cat")
pets.append("bird")
pets.insert(1,"lizard")
print(pets)

"""
### Removing Items ###

Given the list ['apple', 'banana', 'cherry', 'date'], write a program that removes 'banana' using the remove() method and 'date' using the pop() method. 
Print the final list after these operations.
"""
# Write your solution here
list_of_fruits = ['apple', 'banana', 'cherry', 'date']
list_of_fruits.remove("banana")
list_of_fruits.pop(2)
print(list_of_fruits)

"""
### Sort Method and Sorting Function ###

Create a list of integers like: [5, 2, 9, 1, 5, 6].
Sort this list using the sort() method and then print it.
Next, use the sorted() function on the list ['orange', 'apple', 'banana'] and print the result.
"""
# Write your solution here
integers = [5,2,9,1,5,6]
integers.sort()
print(integers)

list_of_unsorted_fruits = ['orange', 'apple', 'banana']
print(sorted(list_of_unsorted_fruits))

"""
### Min, Max, and Sum Functions ###

Given a list of numbers [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
Print the minimum, maximum, and sum of the list.
"""

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Write your solution here
smallest = min(list_of_numbers)
greatest = max(list_of_numbers)
list_sum = sum(list_of_numbers)
print("Minimum: ", smallest)
print("Maximum: ", greatest)
print("Sum: ", list_sum)
"""
### Slicing Lists Without Step and With Step ###

Create a list of the first 10 even numbers. Slice and print the first half of the list.
Then, slice and print every second number from the sliced list.
"""

# WITHOUT STEP
even_numbers = [2,4,6,8,10,12,14,16,18,20]
print(even_numbers[:5])

# WITH STEP
print(even_numbers[:5:2])