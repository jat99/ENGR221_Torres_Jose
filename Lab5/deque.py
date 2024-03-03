"""
Author: Jose Torres
File name: deque.py
Description: Implementation of Deque data structure with a doubly linked list
Date: 2/27/2024
"""

from doublyLinkedList import DoublyLinkedList

class Deque():
    def __init__(self):
        self.__values = DoublyLinkedList() #Creating an object of Class DoublyLinkedList

    #Call functions from DoublyLinkedList Class 
    def isEmpty(self):
        #returns bool
        return self.__values.isEmpty() 
    
    def __len__(self):
        return len(self.__values) #return the length of the list
    
    #overrides the print functions. prints the list with <-> to represent linking
    def __str__(self):
        return str(self.__values)

    #Check the first element of DoublyLinkedList
    def peekLeft(self):
        #returns the value of first element - Int
        return self.__values.first() 

    #Check the last value of DoublyLinkedList
    def peekRight(self):
        #returns the value of Last element - Int
        return self.__values.getLastNode().getValue()

    #Inset at the front of the list
    def insertLeft(self, value):
        #no return here. 
        self.__values.insertFront(value)
    
    #Insert at the end of the list
    def insertRight(self, value): 
        self.__values.insertBack(value)

    #Deletes the first node
    def removeLeft(self): 
        #returns the value of node being deleted - Int
        return self.__values.deleteFirstNode() 

    #Deletes the last node
    def removeRight(self):
        #returns value of node being deleted - Int
        return self.__values.deleteLastNode() 
    
if __name__ == "__main__":
    pass