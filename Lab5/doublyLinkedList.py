"""
Author: Jose Torres
File name: doublyLinkedList.py
Description: Custom Implementation of Doubly Linked List
Date: 2/27/2024

"""

from doubleNode import DoubleNode 

class DoublyLinkedList():

    def __init__(self):
        self.__firstNode = None
        self.__lastNode = None 

    def isEmpty(self):
        return self.getFirstNode() == None

    #value of first node
    def first(self):
        if self.isEmpty():
            raise Exception("Error: List is empty, cannot return first  value")
        return self.getFirstNode().getValue()
    
    def getFirstNode(self):
        return self.__firstNode

    def getLastNode(self):
        return self.__lastNode
    
    def setFirstNode(self, node):
        if type(node) != DoubleNode and node != None:
            raise Exception("Error: Input must be a valid DoubleNode or None")
         
        self.__firstNode = node 

    def setLastNode(self, node):
        if type(node) != DoubleNode and node != None:
            raise Exception("Error: Input must be a valid DoubleNode or None")
        self.__lastNode = node 

    def find(self, value):
    # Traverse down the list, starting with the first node
        node = self.getFirstNode()
        while node != None:
            # If this node has the given value, return it
            if node.getValue() == value:
                return node 
            # Otherwise, grab the next node to check
            node = node.getNextNode()
        # If the value was not found, return None
        return None

    def insertFront(self, value):
       node = DoubleNode(value)
       if self.isEmpty():
            self.setFirstNode(node)
            self.setLastNode(node)
       else:
           node.setNextNode(self.getFirstNode())
           self.getFirstNode().setPreviousNode(node)
           self.setFirstNode(node)    

    def insertBack(self, value):
        if self.isEmpty():
            node = DoubleNode(value, self.getFirstNode(),self.getLastNode())
            self.setFirstNode(node)
            self.setLastNode(node)
        else:
           node = DoubleNode(value, None, self.getLastNode())
           self.getLastNode().setNextNode(node)
           self.setLastNode(node)

    def find(self, value):
        # Traverse down the list, starting with the first node
        node = self.getLastNode()
        while node != None:
            # If this node has the given value, return it
            if node.getValue() == value:
                return node 
            # Otherwise, grab the next node to check
            node = node.getPreviousNode()
        # If the value was not found, return None
        return None

    def insertAfter(self, value_to_add, after_value) -> None:
        node = self.find(after_value) #Retrun node that we want to insert after

        if node == None: return False

        next = node.getNextNode()
        newNode = DoubleNode(value_to_add, next, node)
        node.setNextNode(newNode)

        if next == None: self.setLastNode(newNode)
        else: next.setPreviousNode(newNode)
   
        return True

    def deleteFirstNode(self):
        if self.isEmpty():
            raise Exception("Error: List is empty")
        
        first = self.getFirstNode()

        if first.isLast():
           self.setFirstNode(None)
           self.setLastNode(None)
           return first.getValue()
        
        first.getNextNode().setPreviousNode(None)
        self.setFirstNode(first.getNextNode())

        return first.getValue()
    
    def deleteLastNode(self):
       if self.isEmpty():
           raise Exception("Error: List is empty")
       
       last = self.getLastNode()

       if last.isFirst(): #Check if it is also the first item
           self.setFirstNode(None)
           self.setLastNode(None)
           return last.getValue()

       last.getPreviousNode().setNextNode(None)
       self.setLastNode(last.getPreviousNode())

       return last.getValue()
    
    def deleteValue(self, value):
        if self.isEmpty(): #Check List is not empty
            raise Exception("Error: Cannont delete from empty list")
        previous = self.getFirstNode()
        while previous.getNextNode() != None:
            next = previous.getNextNode() 
            if value == next.getValue():
                #To remove a node, make sure previous and next nodes point to eachother
                next.getNextNode().setPreviousNode(previous)
                previous.setNextNode(next.getNextNode())

                return value
            previous = next
        raise Exception("Error: Cannot find value {} in list".format(value))

    def forwardTraverse(self):
        # Traverse starting from the first node
        node = self.getFirstNode()
        # Stop when we reach the end of the list
        while node != None:
            # Print the value of this node
            print(node.getValue())
            # Update node to be the next node
            node = node.getNextNode()

    def reverseTraverse(self):
        # Traverse starting from the last node
        node = self.getLastNode()
        # Stop when we reach the end of the list
        while node != None:
            # Print the value of this node
            print(node.getValue())
            # Update node to be the previous node
            node = node.getPreviousNode()

    def __len__(self): #This function can work with forward or reverse traverse
        # A counter starting at 0
        l = 0
        # Traverse down the list starting with the first node
        node = self.getFirstNode() 
        # Stop when we reach the end of the list
        while node != None:
            # Increment the counter for each node we find
            l += 1
            # Update node to be the next node
            node = node.getNextNode()
        # Return the counter
        return l 
    
    def __str__(self) -> str:
        # Begin the string with the left bracket
        out = "["
        # Traverse down the list starting with the first node
        node = self.getFirstNode() 
        # Stop when we reach the end of the list
        while node != None:
            # Only add the arrow if there's more than one value in the list
            if len(out) > 1:
                out += " <-> " #Since it is Doubly, it should have two arrows
            # Add the value of the current node to the string
            out += str(node)
            # Update node to be the next node
            node = node.getNextNode()
        # Add the closing bracket and return the string
        return out + "]"
    
    
if __name__ == "__main__":

    dLL = DoublyLinkedList()

    dLL.insertFront(1)
    dLL.insertFront(2)
    dLL.insertBack(3)
    dLL.insertBack(4)
    dLL.deleteFirstNode()
    dLL.insertFront(5)
    dLL.deleteLastNode()
    print(dLL)

    