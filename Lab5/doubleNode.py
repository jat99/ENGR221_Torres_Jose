"""
WRITE YOUR PROGRAM HEADER HERE
"""

class DoubleNode():

    def __init__(self, value, next=None, previous=None):
        self.__value = value
        self.__nextNode = next
        self.__previousNode = previous 

    #####
    # Methods
    #####
        
    def isFirst(self) -> bool:
        pass
        
    def isLast(self) -> bool:
        pass

    #####
    # Getters
    #####

    def getValue(self):
        pass
    
    def getNextNode(self):
        pass

    def getPreviousNode(self):
        pass

    #####
    # Setters
    #####

    def setValue(self, new_value) -> None:
        pass

    def setNextNode(self, new_next) -> None:
        pass

    def setPreviousNode(self, new_previous) -> None:
        pass

    #####
    # Helpers
    #####

    def __checkValidNode(self, node) -> bool:
        if type(node) != DoubleNode and node != None:
            raise Exception("Error: Input must be a valid DoubleNode or None")
        return True
    
    def __str__(self):
        pass

if __name__ == "__main__":
    pass