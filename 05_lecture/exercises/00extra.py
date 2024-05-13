"""
Advanced Exercises, focussing on Lists
"""

"""
### Exercise 1: List Filtering ###

Write a program that initializes a list of integers. Use a loop to fill the list with numbers from 1 to 20.
Then, using list comprehension, create a new list that only includes even numbers from the original list.
Print the original and the filtered lists.

Example Output:
    Original list: [1, 2, 3, ..., 20]
    Filtered list: [2, 4, 6, ..., 20]
"""

# Write your solution here
# original_list = []
# for i in range(1,21):
#     original_list.append(i)
# print(f"Original list: {original_list}")

original_list = list(range(1, 21))
print(f"Original list: {original_list}")

filtered_list = []
for i in range(1,21):
    if i % 2 == 0:
        filtered_list.append(i)
print(f"Filtered list: {filtered_list}")

"""
### Exercise 2: Todo List Application ###

Create a simple todo list application. Start with an empty list named "todos". 
Allow the user to continuously add new tasks to the list by typing them into the console. 
The user can also type 'done' to stop adding tasks, 'remove' to remove the last task, or 'view' to display all tasks.
Use a loop to handle these inputs and modify the list accordingly. 
If 'done' is typed, print the final list of tasks and exit the loop.

Example Interaction:
    Please enter a task or command: >> Buy milk
    Task added.
    Please enter a task or command: >> Do homework
    Task added.
    Please enter a task or command: >> view
    Current tasks: ['Buy milk', 'Do homework']
    Please enter a task or command: >> remove
    Last task removed.
    Please enter a task or command: >> view
    Current tasks: ['Buy milk']
    Please enter a task or command: >> done
    Final tasks: ['Buy milk']
    Exiting...
"""

# Write your solution here
todos = []
while True:
    user_input = input("Please enter a task or command: ")
    if user_input == "done":
        break
    elif user_input == "remove":
        todos.pop(-1)
        print("Last task removed.")
        continue
    elif user_input == "view":
        print("Final tasks:", todos)
    else:
        todos.append(user_input)
        continue
print("Current tasks: ", todos)

"""
### Exercise 3: Analyzing Numbers ###

Create a program that initializes a list with numbers (you can hard code them or get them from the user).
Write a function that receives this list and returns a new list with the following items:
    - 'max': Maximum value in the list
    - 'min': Minimum value in the list
    - 'average': Average of the numbers
    - 'under_avg': A new list inside the list, containing the numbers from the original list that are below the average
Use loops and conditionals to compute these values and store them in the new list.
Print the list at the end.

Example Input: [1, 2, 3]
Example Output: [3, 1, 2, [1]]

BONUS TASK:
If you want, you can research "dictionaries" in Python and structure your solution like that:
    {
        'max': 3,
        'min': 1,
        'average': 2,
        'under_avg': [1]
    }
"""

# Write your solution here
def analyzing_numbers(numbers):
    greatest = max(numbers)
    smallest = min(numbers)
    average = sum(numbers) / len(numbers)
    # LIST COMPREHENSION is used to create a new list that contains only the numbers that are less than the average
    under_avg = [num for num in numbers if num < average]
    return {'max': greatest, 'min': smallest, 'average': average, 'under_avg': under_avg}

#my_list = int(input("Input numbers: ")) ???????
my_list = [2,5,4,7]
print(f"Output: {analyzing_numbers(my_list)}")


# COPILOT:
# def calculate_stats(numbers):
#     max_value = max(numbers)
#     min_value = min(numbers)
#     average = sum(numbers) / len(numbers)
#     under_avg = [num for num in numbers if num < average]
#
#     return {'max': max_value, 'min': min_value, 'average': average, 'under_avg': under_avg}
#
# # Initialize the list with numbers
# numbers = [1, 2, 3]  # Example input
#
# # Get the statistics
# stats = calculate_stats(numbers)
#
# # Print the statistics
# print(stats)
