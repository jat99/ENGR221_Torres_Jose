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
            self.__length = initialSizeOrElements  # Start with given number of values
            self.__maxLength = initialSizeOrElements # Start with given number of values
        else: 
            self.__a = initialSizeOrElements # Set a equal to list that is passed in
            self.__length = len(initialSizeOrElements) # Set length equal to the size of the list passed in
            self.__maxLength = self.__length # Set maxLength eqaul to length

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
        if self.__maxLength <= self.__length: # Check if there is enough space in array
            self.__a += [None] * 2 # Increase size of array by two (Can be any value)
            self.__maxLength = len(self.__a) # Update max length

        self.__a[self.__length] = value #insert the value at the current size of length
        self.__length += 1 #increment the length by 1
           
    

    # Return the index of value in the array, 
    # or -1 if value is not in the array
    def search(self, value):
        # Only search the indices we've inserted
        indexes = [] # Start with empty array to collect all indexes of duplicates
        for idx in range(self.__length): 
            # Check the value at the current index 
            if self.__a[idx] == value:  
                indexes.append(idx) # if values match then add index to array   
        return indexes  # Return the indexes                   

    # Delete the first occurrence of value in the array
    # Returns True if value was deleted, False otherwise
    def delete(self, value):
        # Find the index of the value to delete
        idx = self.search(value) # Get array of indexes that are duplicates
        
        # Loop through array of indexes
        for i in range(len(idx)):    
            if i != 0: # decrement the index by one after the first index because array will be shifted
                idx[i] = idx[i] - 1
            # Decrement the array length
            self.__length -= 1

            # Shift all the remaining values 
            for j in range(idx[i], self.__length):
                self.__a[j] = self.__a[j+1]
            # if the array is done looping then recreate the array to remove the excess values
            if i == len(idx) - 1:
                self.__a = self.__a[0:self.__length]
   
    # Print all items in the list
    def traverse(self):
        for i in range(self.__length):
            print(self.__a[i])

if __name__ == '__main__':
    print("Jose Torres")
    pass
