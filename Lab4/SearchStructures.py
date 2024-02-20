"""
WRITE YOUR PROGRAM HEADER HERE
"""

# Implementation of a Stack
class Stack():
    def __init__(self):
        self.__items = []
        self.__length = len(self.__items)

    # Returns True if the Stack is empty, or False if it is not empty
    def isEmpty(self):
        return  self.__length == 0

    def values(self):
        print(" ")
        for i in range(self.__length):
            print(self.__items[i].getRow(), self.__items[i].getCol())
    # For a Stack, this should "push" item to the top of the Stack
    def add(self, item):
        self.__items += [item]
        self.__length += 1
    
    def current(self):
        return self.__items[self.__length - 1]

    # For a Stack, this should "pop" an item from the Stack
    # and return it
    def remove(self):
        value = self.__items[self.__length - 1]
        self.__length -= 1
        self.__items = self.__items[0:self.__length]
        return value
    
# Implementation of a Queue
class Queue():
    def __init__(self):
        self.__items = []
        self.__length = len(self.__items)

    # Returns True if the Queue is empty, or False if it is not empty
    def isEmpty(self):
        return self.__length == 0

    def current(self):
        return self.__items[0]

    # For a Queue, this should "enqueue" item to the end of the Queue
    def add(self, item):
        self.__items += [item]
        self.__length += 1

    def value(self):
        return self.__items[0]

    # For a Queue, this should "dequeue" an item from the Queue
    # and return it
    def remove(self):
        value = self.__items[0]
        self.__items = self.__items[1:self.__length]
        self.__length -= 1
        
        return value
        
    
if __name__ == '__main__':
    q = Queue()
    # Add five items to the queue
    for i in range(5):
        q.add(i)
    items_removed = []
    # Remove items from the queue
    while not q.isEmpty():
        items_removed.append(q.remove())

    print(items_removed)
    pass