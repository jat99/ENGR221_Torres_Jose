"""
Name: Jose Torres
Filename: myset.py
Date: 02/06/2023

"""

class MySet:

    def __init__(self, values):
        self.set = []
        self.length = 0
        self.max_length = 0
        for i in range(len(values)):
            self.insert(values[i])
    
    def size(self):
        return self.length
    
    def vals(self):
        return self.set
                
    def search(self, value):
        for i in range(self.length):
            if value == self.set[i]:
                return True
        return False
    
    def search_temp(self, value, values):
        tempSet = values
        for j in range(len(tempSet)):
            if value == tempSet[j]:
                return True
        return False
    
    def insert(self, value):
        if self.search(value) == False:
            if self.length >= self.max_length:
                self.set += [None] * 1
                self.max_length = len(self.set)
            self.set[self.length] = value
            self.length += 1

    def traverse(self):
       if self.isEmpty():
            print("Set is Empty!")
       else: 
            for i in range(self.length):
                print(self.set[i])

    def delete(self, value):
        if self.isEmpty():
            print("Nothing to delete, set is empty!")
        else: 
            for i in range(self.length):
                if value == self.set[i]:
                    self.swap(i)
                    return

    def swap(self, i):
        self.set[i] = self.set[self.length - 1]
        self.set = self.set[0:self.length]
        self.length -= 1

    def isSet(self,values):
        temp_set = []
        for i in range(len(values)):
            if self.search_temp(values[i],temp_set) == True:
                return False
            temp_set.append(values[i])
        return True

    def isEmpty(self):
        if self.length > 0:
            return False
        return True
    
if __name__ == '__main__':
    pass