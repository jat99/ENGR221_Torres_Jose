"""
Author: Jose Torres
File name: SearchStructures.py
Description: Custom Implemenation of Stack and Queue Data Structure
Date: 2/27/2024
"""

# Implementation of a Stack
class Stack():
    def __init__(self):
        self.__items = []
        self.__length = len(self.__items)

    # Returns True if the Stack is empty, or False if it is not empty
    def isEmpty(self):
        return  self.__length == 0
    
    # For a Stack, this should "push" item to the top of the Stack
    def add(self, item):
        self.__items += [item] #insert to end of array
        self.__length += 1
    
    # For a Stack, this should "pop" an item from the Stack
    # and return it
    def remove(self):
        #store value to be removed
        value = self.__items[self.__length - 1]
        self.__length -= 1 #decrement the length
        self.__items = self.__items[0:self.__length] #create array with new updated length
        return value
    
# Implementation of a Queue
class Queue():
    def __init__(self):
        self.__items = []
        self.__length = len(self.__items)

    # Returns True if the Queue is empty, or False if it is not empty
    def isEmpty(self):
        return self.__length == 0

    # For a Queue, this should "enqueue" item to the end of the Queue
    def add(self, item):
        self.__items += [item] #Same as stack, add to end of array
        self.__length += 1

    # For a Queue, this should "dequeue" an item from the Queue
    # and return it
    def remove(self):
        value = self.__items[0] #Store value of element being remvoed
        self.__items = self.__items[1:self.__length] #Shift or create new array, don't include first element
        self.__length -= 1 #Decrement the length
        
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