"""
WRITE YOUR PROGRAM HEADER HERE
"""

class BinarySearchTree:
    """ DESCRIBE THE BST CLASS HERE """

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

    def isEmpty(self):
        """ ISEMPTY DOCUMENTATION HERE """
        pass
    
    def getRoot(self):
        """ GETROOT DOCUMENTATION HERE """
        pass

    def search(self, goalKey):
        """ SEARCH DOCUMENTATION HERE """
        return self.__searchHelp(self.__root, goalKey)

    def __searchHelp(self, node, goalKey):
        """ __SEARCHHELP DOCUMENTATION HERE """
        pass

    def lookup(self, goal):
        """ LOOKUP DOCUMENTATION HERE """
        pass

    def findSuccessor(self, subtreeRoot):
        """ FINDSUCCESSOR DOCUMENTATION HERE """
        return self.__findSuccessorHelp(subtreeRoot)
    
    def __findSuccessorHelp(self, node):
        """ __FINDSUCCESSOR DOCUMENTATION HERE """
        pass
    
    def delete(self, deleteKey):
        """ DELETE DOCUMENTATION HERE """
        if self.search(deleteKey):
            return self.__deleteHelp(self.__root, deleteKey)
        raise Exception("Key not in tree.")
    
    def __deleteHelp(self, node, deleteKey):
        """ __DELETEHELP DOCUMENTATION HERE """
        pass

    def traverse(self) -> None:
        """ TRAVERSE DOCUMENTATION HERE """
        self.__traverseHelp(self.__root)

    def __traverseHelp(self, node) -> None:
        """ __TRAVERSEHELP DOCUMENTATION HERE """
        pass

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
        
if __name__ == "__main__":
    pass