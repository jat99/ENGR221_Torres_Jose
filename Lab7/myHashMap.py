"""
WRITE YOUR PROGRAM HEADER HERE

Adapted from UCSD CSE12
"""

class MyHashMap:
    def __init__(self, load_factor=0.75,
                       initial_capacity=16):
        self.load_factor = load_factor 
        self.capacity = initial_capacity 
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    """
    Resizes the self.buckets array when the load_factor is reached. """
    def resize(self): 
        # Double the number of buckets 
        self.capacity *= 2 
        # Make a copy of the current contents in the buckets 
        old_buckets = self.buckets 
        # Create a new set of buckets that's twice as big as the old one 
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
         # Add each key, value pair already in the MyHashMap to the new buckets 
        for bucket in old_buckets: 
            if bucket != []: 
                for entry in bucket: 
                    self.put(entry.getKey(), entry.getValue())
 
        

    """
    Adds the specified key, value pair to the MyHashMap if 
    the key is not already in the MyHashMap. If adding a new key would
    surpass the load_factor, resize the MyHashMap before adding the key.
    Return true if successfully added to the MyHashMap.
    Raise an exception if the key is None. """
    def put(self, key, value):
        if type(key) == type(None):
            raise Exception("Error: The key is invalid")

        if len(self.buckets) * self.load_factor <=  self.size + 1:
            self.resize()

        keyHash = self.hashKey(key)
        if len(self.buckets[keyHash]) == 0:
            entry = self.MyHashMapEntry(key, value)
            self.buckets[keyHash].append(entry)  
            self.size+=1
            return True
        
        return False

    """
    Replaces the value that maps to the given key if it is present.
    Input: key is the key whose mapped value is being replaced.
           newValue is the value to replace the existing value with.
    Return true if the key was in this MyHashMap and replaced successfully.
    Raise an exception if the key is None. """
    def replace(self, key, newValue):
        if type(key) == type(None):
            raise Exception("Error: The key is invalid")
        entry = self.MyHashMapEntry(key, newValue)
        self.buckets[self.hashKey(key)][0] = entry
        return True

    """
    Remove the entry corresponding to the given key.
    Return true if an entry for the given key was removed.
    Raise an exception if the key is None. """
    def remove(self, key):
        if type(key) == type(None): 
            raise Exception("Error: The key is invalid")
        self.buckets[self.hashKey(key)] = []
        self.size -=1
        print("hello")
        return True

    """
    Adds the key, value pair to the MyHashMap if it is not present.
    Otherwise, replace the existing value for that key with the given value.
    Raise an exception if the key is None. """
    def set(self, key, value):
        if not (self.put(key, value)):
            self.replace(key, value)
        elif type(key) == type(None):
            raise Exception("Error: The key is invalid")
       

    """
    Return the value of the specified key. If the key is not in the
    MyHashMap, return None.
    Raise an exception if the key is None. """
    def get(self, key):
        if type(key) == type(None):
            raise Exception("Error: The key is invalid")
        if self.buckets[self.hashKey(key)] != []:
            return self.buckets[self.hashKey(key)][0]
        return None

    """
    Return the number of key, value pairs in this MyHashMap. """
    def size(self):
        return self.size

    """
    Return true if the MyHashMap contains no elements, and 
    false otherwise. """
    def isEmpty(self):
        return self.size == 0

    def hashKey(self, key): 
        return abs(hash(key)) % len(self.buckets)
    
    """
    Return true if the specified key is in this MyHashMap. 
    Raise an exception if the key is None. """
    def containsKey(self, key):
        if type(key) == type(None):
            raise Exception("Error: The key is invalid")
        return len(self.buckets[self.hashKey(key)]) == 1

    """
    Return a list containing the keys of this MyHashMap. 
    If it is empty, return an empty list. """
    def keys(self):
        if self.isEmpty():
            return []
        else:
            keys = []
            for bucket in self.buckets:
                if bucket != []:
                    keys.append(bucket[0].getKey())
            return keys

    class MyHashMapEntry:
        def __init__(self, key, value):
            self.key = key 
            self.value = value 

        def getKey(self):
            return self.key 
        
        def getValue(self):
            return self.value 
        
        def setValue(self, new_value):
            self.value = new_value 

if __name__ == "__main__":

    myHashMap = MyHashMap()
    entry1 = MyHashMap.MyHashMapEntry("jose", "hello")
    entry2 = MyHashMap.MyHashMapEntry("anthony", "blah")
    entry3 = MyHashMap.MyHashMapEntry("julius", "hello")
    entry4 = MyHashMap.MyHashMapEntry("jr", "hello")
    entry5 = MyHashMap.MyHashMapEntry("jose", "yessir")

    #print("Is Hash Map Empty?", myHashMap.isEmpty())

    myHashMap.put(entry1.getKey(), entry1.getValue())
    myHashMap.put(entry2.getKey(), entry2.getValue())
    myHashMap.put(entry3.getKey(), entry3.getValue())
    myHashMap.put(entry4.getKey(), entry4.getValue())
    #myHashMap.remove(entry1.getKey())
    
    #print("Is Hash Map Empty?", myHashMap.isEmpty())
    #print(myHashMap.buckets)
    #print(myHashMap.size)
    #print(myHashMap.containsKey(entry2.getKey())) 
    print(myHashMap.get("jose"))
    #myHashMap.put("joey", "hello")
    #myHashMap.put("joe", "worker")


 

    pass