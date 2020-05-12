from Task import *
toDo = PriorityQueue()
task2 = Task("revision CA", '512', reading)
task1 = Task("java assignment", '511', assignment)
task3 = Task("edit photos", '513', partTime)
task4 = Task("quiz ten, dsa", '512', assignment)

toDo.insert(task2.getNode())
toDo.insert(task1.getNode())
toDo.insert(task3.getNode())
toDo.insert(task4.getNode())


toDo.print()