
class MySet:

    def __init__(self, values):
        self.set = { }
        for i in range(len(values)):
            self.set[values[i]] = True

    def search(self, value):
        try: 
            return self.set[value]
        except:
            return False
    
    def insert(self, value):
       if (self.search(value) == False):
            self.set[value] = True
    
    def delete(self, value):
        if self.search(value):
            del self.set[value]

    def traverse(self):
        for i in self.set.keys():
            print(i)

if __name__ == '__main__':
    mySet = MySet([1,2,3,5,5])
    mySet.insert(6)
    mySet.delete(2)
    print(mySet.set)
    mySet.traverse()
    pass