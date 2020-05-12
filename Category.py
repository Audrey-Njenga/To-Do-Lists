# implements a rank for each category, the higher the rank, the higher the priority for the task
class Category:
    def __init__(self, title, rank):
        self.title = title
        self.weight = rank


assignment = Category("assignment", 0.1)
reading = Category("reading", 0.2)
partTime = Category("part-time", 0.3)
leadership = Category("leadership", 0.4)
hobby = Category("hobby", 0.5)



