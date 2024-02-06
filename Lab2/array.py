"""
Author: Prof. Alyssa
Filename: array.py
Description: Implementation of an unsorted array with duplicates
"""

class Array():
    # Constructor
    def __init__(self, initialSizeOrElements):
        if type(initialSizeOrElements) == int:
            self.__a = [None] * initialSizeOrElements # The array stored as a list
            self.__length = initialSizeOrElements  # Start with no values in the list
            self.__maxLength = initialSizeOrElements
        else: 
            self.__a = initialSizeOrElements
            self.__length = len(initialSizeOrElements)
            self.__maxLength = self.__length

    ########
    # Methods
    ########
        
    # Return the current length of the array
    def length(self):
        return self.__length 
    
    # Return a list of the current array values
    def values(self):
        return self.__a

    # Return the value at index idx
    # Otherwise, do not return anything
    def get(self, idx):
      if 0 <= idx and idx < self.__length: # Check if idx is in bounds, and
         return self.__a[idx]              # only return item if in bounds
 
    # Set the value at index idx
    def set(self, idx, value):         
      if 0 <= idx and idx < self.__length: # Check if idx is in bounds, and
         self.__a[idx] = value               # only set item if in bounds
    
    # Insert value to the end of the array
    def insert(self, value):
        if self.__maxLength <= self.__length:
            self.__a += [None] * 2
            self.__maxLength = len(self.__a)

        self.__a[self.__length] = value
        self.__length += 1
           
    

    # Return the index of value in the array, 
    # or -1 if value is not in the array
    def search(self, value):
        # Only search the indices we've inserted
        indexes = []
        for idx in range(self.__length): 

            # Check the value at the current index 
            if self.__a[idx] == value:  
                indexes.append(idx)
                # Return the index               
        return indexes                        

    # Delete the first occurrence of value in the array
    # Returns True if value was deleted, False otherwise
    def delete(self, value):
        # Find the index of the value to delete
        idx = self.search(value)
        
        # If the value was found
        for i in range(len(idx)):    
            if i != 0:
                idx[i] = idx[i] - 1
            # Decrement the array length
            self.__length -= 1

            # Shift all the remaining values 
            for j in range(idx[i], self.__length):
                self.__a[j] = self.__a[j+1]

            if i == len(idx) - 1:
                self.__a = self.__a[0:self.__length]
   
    # Print all items in the list
    def traverse(self):
        for i in range(self.__length):
            print(self.__a[i])

if __name__ == '__main__':
    print("Jose Torres")
    pass
