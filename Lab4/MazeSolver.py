"""Author: Jose Torres
File name: MazeSolver.py
Description: Solved a maze using DFS(stack) and BFS(queue)
Date: 2/27/2024
"""

from SearchStructures import Stack, Queue
from Maze import Maze

class MazeSolver:
    # Constructor
    # Inputs:
    #   maze: The maze to solve (Maze)
    #   searchStructure: The search structure class to use (Stack or Queue)
    def __)init__(self, maze, searchStructure):
        self.maze = maze             # The maze to solve
        self.ss = searchStructure()  # Initialize a searchStructure object

    def tileIsVisitable(self, row:int, col:int) -> bool:
        #check if out of bounds
        if row >= self.maze.num_rows or row < 0:    return False
        if col >= self.maze.num_cols or col < 0:    return False
        if self.maze.contents[row][col].visited():  return False
        if self.maze.contents[row][col].isWall():   return False
   
        return True

    def solve(self):
        #add starting point to stack
        self.ss.add(self.maze.start)
        
        while not self.ss.isEmpty():
            
            #retrieve the next node to check and also remove it
            current = self.ss.remove()
            
            #mark the new node as visited
            self.maze.contents[current.getRow()][current.getCol()].visit()

            #once goal is found, terminate the function
            if current == self.maze.goal:
                return 
            else: 
                if (self.tileIsVisitable(current.getRow() - 1, current.getCol())): #NORTH
                    self.maze.contents[current.getRow() - 1][current.getCol()].setPrevious(current) #Set previous to current
                    self.ss.add(self.maze.contents[current.getRow() - 1][current.getCol()]) #Insert into stack if visitable

                if (self.tileIsVisitable(current.getRow() + 1, current.getCol())): #SOUTH
                    self.maze.contents[current.getRow() + 1][current.getCol()].setPrevious(current)
                    self.ss.add(self.maze.contents[current.getRow() + 1][current.getCol()])

                if (self.tileIsVisitable(current.getRow(), current.getCol() + 1)): #EAST
                    self.maze.contents[current.getRow()][current.getCol() + 1].setPrevious(current)
                    self.ss.add(self.maze.contents[current.getRow()][current.getCol() + 1])

                if (self.tileIsVisitable(current.getRow(), current.getCol() - 1)): #WEST
                    self.maze.contents[current.getRow()][current.getCol() - 1].setPrevious(current)
                    self.ss.add(self.maze.contents[current.getRow()][current.getCol() - 1])
        return #end function once all nodes have been visited - no path was found/formed

    def getPath(self):
        
        current = self.maze.goal

        if current.getPrevious() == None: return []

        array = []

        while (current != None):
            array.append(current)
            current = current.getPrevious()

        return array 
    
    # Print the maze with the path of the found solution
    # from Start to Goal. If there is no solution, just
    # print the original maze.
    def printSolution(self):
        # Get the solution for the maze from the maze itself
        solution = self.getPath()
        
        # A list of strings representing the maze
        output_string = self.maze.makeMazeBase()
        # For all of the tiles that are part of the path, 
        # mark it with a *
        for tile in solution:
            output_string[tile.getRow()][tile.getCol()] = '*'
        # Mark the start and goal tiles
        output_string[self.maze.start.getRow()][self.maze.start.getCol()] = 'S'
        output_string[self.maze.goal.getRow()][self.maze.goal.getCol()] = 'G'

        # Print the output string
        for row in output_string:
            print(row)

   

if __name__ == "__main__":
    # The maze to solve
    maze = Maze(["##____#_##",
                 "#____##__#",
                 "_S#_______",
                 "__##_____#",
                 "____####__",
                 "#____##___",
                 "#__##___#_",
                 "___##___##",
                 "#___#__G__",
                 "_______###"])
    # Initialize the MazeSolver to be solved with a Stack
    solver = MazeSolver(maze, Stack)

    solver.solve()
    # Print the solution found
    solver.printSolution()