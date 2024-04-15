"""
Name: Jose Torres
Date: 04/14/2024
File: BinarySearchTree.py
Description: Binary Search Tree Class that allows insertion, deletion and searching in log(n) time
"""

class BinarySearchTree:
    """ 
    Binary Search Tree Class allows for insertion, deletion, search and traversal
    Uses node custom class to define the data that will be stored in tree
    Uses recursion to achieve main functionalities making it more efficient under 
    certain condtions
    """

    def __init__(self):
        self.__root = None # The root Node of this BST

    def insert(self, insertKey, insertValue):
        """ Inserts the given key and value into the BST.
            Inputs:
                - insertKey: (any) The key to insert
                - insertValue: (any) The value to insert
            Returns: None
        """
        # Update the root to include the inserted node
        self.__root = self.__insertHelp(self.__root, insertKey, insertValue)
    
    def __insertHelp(self, node, insertKey, insertValue):
        """ A recursive helper method to insert a new node 
            with the given key and value into the BST.
            Inputs:
                - node: (Node) The root of the subtree to insert into
                - insertKey: (any) The key to insert
                - insertvalue: (any) The value to insert
            Returns: The node to insert """
        # Base case - Insert the node as a leaf in the appropriate location
        if node == None:
            return self.__Node(insertKey, insertValue)
        # Insert the key into the left subtree if it is less than the current key
        elif insertKey < node.key:
            node.left = self.__insertHelp(node.left, insertKey, insertValue)
        # Insert the key into the right subtree if it is greater than the current key
        elif insertKey > node.key:
            node.right = self.__insertHelp(node.right, insertKey, insertValue)
        # Return the node with the node inserted
        return node

    #tree is empty when the first node is None
    def isEmpty(self): 
        return self.__root == None
    
    def getRoot(self):
        return self.__root

    def search(self, goalKey):
        """ 
        Returns the value returned from search help
        """
        return self.__searchHelp(self.__root, goalKey)

    def __searchHelp(self, node, goalKey):
        """ 
        Recursive function that keeps calling itself until either a node 
        was found or not. 
        4 possible cases.
        """
        if node == None:
            return None
        elif node.key == goalKey:
            return node
        elif node.key < goalKey:
            return self.__searchHelp(node.right, goalKey)
        elif node.key > goalKey:
            return self.__searchHelp(node.left, goalKey)

    #returns the result from searchHelp
    def lookup(self, goal):
        """ 
        This function just returns value from node returned from search
        """
        return self.search(goal).value

    #returns the smallest number after root
    def findSuccessor(self, subtreeRoot):
        """ 
        Calls find successor help
        """
        return self.__findSuccessorHelp(subtreeRoot)
    
    def findPredecessor(self, subtreeRoot):
        """ 
        Calls find predecessor help
        """
        return self.__findPredecessorHelp(subtreeRoot)
    
    def __findPredecessorHelp(self, node):
        """ 
        Recursive function that only stops when the right most node of left tree is found 
        """
        if node.right == None:
            return node 
        return self.__findSuccessorHelp(node.right)
    
    def findMin(self, node):
        """ 
        Recursive function that only stops when the left most node of tree is found 
        """
        if node.left == None:
            return node
        return self.findMin(node.left)
    
    def findMax(self, node):
        """ 
        Recursive function that only stops when the right most node of tree is found 
        """
        if node.right == None:
            return node
        return self.findMax(node.right)

    
    #recursive call to search for smallest value in tree
    def __findSuccessorHelp(self, node):
        """ 
        Recursive function that only stops when the left most node of right tree is found 
        """
        if node.left == None:
            return node 
        return self.__findSuccessorHelp(node.left)
    
    #updating root when deleting
    def delete(self, deleteKey):
        """ 
        This function first checks to see if the key is in tree
        If no key is found exception is raised.
        If key exists, then we must call a recursive function that will update 
        starting at the root node
        """
        if self.search(deleteKey):
            self.__root = self.__deleteHelp(self.__root, deleteKey)
        else:
            raise Exception("Key not in tree.")
    
    def __deleteHelp(self, node, deleteKey):
        """ 
        3 cases in this function, 3 sub cases
        Since checking if the key is already in the tree we don't need to account for that 
        First 3 cases are either the key is less then, greater than or equal
        3 sub cases appear when key is equal
        The cases are either the node to be deleted is leaf, has one child or two children
        """
        # 3 cases: 0, 1 or 2 children
        if deleteKey < node.key: #node key is greater, look left
            node.left = self.__deleteHelp(node.left,deleteKey)
        elif deleteKey > node.key: #delete key is greater, look right
            node.right = self.__deleteHelp(node.right,deleteKey)
        else:
            if (node.left == None and node.right == None): #no children
                node = None
            elif (node.left == None): #right child
                node =  node.right
            elif (node.right == None): #left child
                node = node.left
            else: #two children
                tempNode = self.findSuccessor(node.right) #swap with this node
                node.key = tempNode.key
                node.value = tempNode.value
                node.right = self.__deleteHelp(node.right, tempNode.key)
        return node

    def traverse(self) -> None:
        """ 
        Calls Traverse Help to perform recursion
        """
        # BFS vs DFS
        self.__traverseHelp(self.__root)

    def __traverseHelp(self, node) -> None: #inorder traversal
        """ 
        Since we want to print the items in order then inorder 
        traversal must be used. You visited the left most node then print,
        then visit the right
        This is a form of DFS.
        """
        if type(node) == self.__Node:
            self.__traverseHelp(node.left)
            print(node)
            self.__traverseHelp(node.right)

    def __str__(self) -> str:
        """ Represent the tree as a string. Formats as 
            {(rootkey, rootval), {leftsubtree}, {rightsubtree}} """
        return self.__strHelp("", self.__root)
    
    def __strHelp(self, return_string, node) -> str:
        """ A recursive helper method to format the tree as a string. 
            Input: 
                - return_string: (string) Accumulates the final string to output
                - node: (Node) The current node to format
            Returns: A formatted string for this node. """
        # Base case - Represent an empty branch as "None"
        if node == None:
            return "None"
        # Recursively build the string to return
        # Note, this is equivalent to
        #   return "{" + node + ", " + \
        #                self.strHelp(return_string, node.left) + ", " + \
        #                self.strHelp(return_string, node.right) + "}"
        return "{{{}, {}, {}}}".format(node, 
                                       self.__strHelp(return_string, node.left), 
                                       self.__strHelp(return_string, node.right))
            

    ##############
    # NODE CLASS #
    ##############

    class __Node:
        """ Implementation of a node in a BST. Note that it is 
            private, so it cannot be accessed outside of a BST """

        def __init__(self, key, value, left=None, right=None):
            self.key = key         # The key of the root node of this tree
            self.value = value     # The value held by the root node of this tree
            self.left = left       # Points to the root of the left subtree
            self.right = right     # Points to the root of the right subtree

        def __str__(self):
            """ Represent the node as a string.
                Formats as "{key, value}" """
            return "({}, {})".format(self.key, self.value)

class Nodes:
   def __init__(self):  
       print("initialize")

if __name__ == "__main__":
    bst = BinarySearchTree()
    #bst.insert(5, 5)
    bst.insert(5, 5)
    bst.insert(8, 8)
    bst.insert(3,3)
    bst.insert(1,1)
    bst.insert(0,0)
    bst.insert(10,10)
    bst.insert(7,7)

    bst.traverse()
    print("---------------")

    print(bst.findMin(bst.getRoot()))
    print(bst.findMax(bst.getRoot()))


