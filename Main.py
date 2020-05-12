from Task import Task
print("Hi, Welcome to the To Do App.")
print("-" * 15)
print("Your To Do List:")

choice = int(input("What would you like to do today?\n"
                   "Enter 1 to add an item to the to do list\n"
                   "Enter 2 to remove an item from the to do list\n"))

if choice == 1:
    task = input("Enter task to be done: ")
    deadline = int(input("Enter the deadline in format MMDD: "))
    cat = input("Enter the category of the task \n (assignment, reading, hobby, part-time or leadership: ")

    Task(task, deadline, cat)



