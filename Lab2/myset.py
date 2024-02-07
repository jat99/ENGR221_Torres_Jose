"""
Name: Jose Torres
Filename: myset.py
Date: 02/06/2023

"""

class MySet:

    #Constructor
    def __init__(self, values):
        self.set = []
        self.length = 0
        self.max_length = 0
        for i in range(len(values)): # Loop length of list
            self.insert(values[i]) # Insert values into function
    
    #Return size of set
    def size(self):
        return self.length
    
    #Return values in set
    def vals(self):
        return self.set

    #Loop array and check if there is match           
    def search(self, value):
        for i in range(self.length):
            if value == self.set[i]:
                return True
        return False
    
    #Insert function
    def insert(self, value):
        if self.search(value) == False: #Run search and only proceed if item is not in set
            if self.length >= self.max_length:
                self.set += [None] * 1 # Update set to accomdate for one addition
                self.max_length = len(self.set) # Update max length, can also increment by one
            self.set[self.length] = value
            self.length += 1

    def traverse(self):
       if self.isEmpty(): #Check if set is empty
            print("Set is Empty!")
       else: 
            for i in range(self.length): # Loop the length of the set
                print(self.set[i])

    def delete(self, value):
        if self.isEmpty(): # Check if set is empty
            print("Nothing to delete, set is empty!")
        else: 
            for i in range(self.length): #Loop though set
                if value == self.set[i]: #If there is a match then swap values and update lengths
                    self.swap(i)
                    return
                
    #swaps the values at final and matched index, since order does not matter
    def swap(self, i):
        self.set[i] = self.set[self.length - 1]
        self.set = self.set[0:self.length]
        self.length -= 1 # Decrement length
        
    #Check if set is empty
    def isEmpty(self):
        if self.length > 0: # if length is greater than 0, than set is not empty
            return False
        return True
    
if __name__ == '__main__':
    pass