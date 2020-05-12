import random
from Task import *
to_do = PriorityQueue()


def Category(cat):
    cat = int(cat)
    if cat == 1:
        return assignment
    elif cat == 2:
        return reading
    elif cat == 3:
        return partTime
    elif cat == 4:
        return leadership
    elif cat == 5:
        return hobby
    else:
        return "Invalid choice"
        Menu()


def Process(choice):
    count = 0
    if choice == 1:
        print("Hint: Break down tasks into small achievable tasks for longer tasks")
        task = input("Enter task to be done: ")
        deadline = input("Enter deadline in format MMDD: ")
        category = input("Choose category of the task: \n Enter 1 for assignment \n "
                         "Enter 2 for reading \n Enter 3 for part-time \n"
                         "Enter 4 for leadership\n Enter 5 for hobby\n")
        to_do.insert(Task(task, deadline, Category(category)).getNode())
        count += 1
        print("Successfully inserted")
        ans = input("Would you like to return to the main menu? (Yes/No)").lower()
        print("-"*20)
        rerun(ans)

    elif choice == 2:
        to_do.delete()
        print("Successfully deleted")
        ans = input("Would you like to return to the main menu? (Yes/No)").lower()
        print("-" * 20)
        rerun(ans)

    else:
        ans = input("invalid choice. Would you like to return to the main menu? (Yes/No)").lower()
        rerun(ans)


def Menu():
    if to_do.isEmpty():
        print("Nothing in to do list :)")
    else:
        print("Your To-Do List is: \n")
        to_do.print()
    print("-" * 20)
    choice = (input("What would you like to do today?\n"
                    "Enter 1 to add an item to the to do list\n"
                    "Enter 2 to remove completed item at top of the list\n"))
    return int(choice)


def rerun(ans):
    mot = ["Stay motivated", "Great things take hard work", "Challenge yourself", "Just start"]

    if ans == "yes" or ans == "yeah" or ans == "y":
        Process(Menu())
    else:
        print("Thank you for using the app. \n Quote of the day: " + mot[random.randint(0, 3)])
        exit()



