from Category import *


class Task:
    # node that holds the task details

    def __init__(self, name, deadline, category):
        self.name = name
        self.deadline = deadline
        self.category = category

    # creates a weight based on the deadline and category rank
    def getWeight(self):
        return self.category.weight + int(self.deadline)

    # creates a tuple to be added to the priority queue
    def getNode(self):
        node = (self.getWeight(), self.name, self.deadline[:1] + "." + self.deadline[1:])
        return node


# binary max heap that takes in an array used to implement priority queue
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def isEmpty(self):
        if not self.heap:
            return True
        else:
            return False

    # returns element at top of heap with O(1) time

    def parent(self, pos):
        parent = pos // 2
        return parent

    def left_child(self, pos):
        left_child = 2 * pos + 1
        return left_child

    def right_child(self, pos):
        right_child = 2 * pos + 2
        return right_child

    # checks if the node is a leaf node, takes in the index of the node
    def isLeaf(self, pos):
        if (len(self.heap) // 2) <= pos <= len(self.heap):
            return True
        else:
            return False

    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    # method is used to maintain heap invariant on deletion
    def heapify(self, pos):
        if not self.isLeaf(pos):
            smallest = pos
            if self.left_child(pos) < len(self.heap) and self.heap[pos] > self.heap[self.left_child(pos)]:
                smallest = self.left_child(pos)
            elif self.right_child(pos) < len(self.heap) and self.heap[pos] > self.heap[self.right_child(pos)]:
                smallest = self.right_child(pos)
            else:
                exit()
            if smallest != pos:
                self.swap(pos, smallest)
                self.heapify(smallest)

    # inserts element into next available position then swaps it till in the right
    # position to maintain min heap
    def insert(self, node):
        self.heap.append(node)
        if len(self.heap) > 1:
            index = len(self.heap) - 1
            while self.heap[index] < self.heap[self.parent(index)]:
                self.swap(index, self.parent(index))
                index = self.parent(index)

    # pop elements from the list and add them to a new list.
    # items are popped in order of priority making new list ordered.
    def print(self):
        heap = self.heap.copy()
        result = []
        least = 0

        def miniHeapify(pos):
            if not (len(heap) // 2) <= pos <= len(heap):
                least_node = pos
                if self.left_child(pos) < len(heap) and heap[pos] > heap[self.left_child(pos)]:
                    least_node = self.left_child(pos)
                elif self.right_child(pos) < len(heap) and heap[pos] > heap[self.right_child(pos)]:
                    least_node = self.right_child(pos)
                else:
                    exit()
                if least_node != pos:
                    heap[pos], heap[least_node] = heap[least_node], heap[pos]
                    miniHeapify(least_node)

        if len(heap) != 0:
            result.append(heap[least])
            heap[least], heap[-1] = heap[-1], heap[least]
            heap.pop(-1)
            miniHeapify(0)
        else:
            result.append(heap[0])

        count = 0
        for x in result:
            count += 1
            print("Task " + str(count) + ": " + x[1] + "\n Deadline: " + str(x[2]) + "\n")

    # uses heapify to maintain heap invariant upon deletion
    def delete(self):
        if len(self.heap) > 0:
            popped = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop(-1)
            self.heapify(0)
            return popped
        else:
            print("Nothing to remove")
            exit()





