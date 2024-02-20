"""
WRITE YOUR PROGRAM HEADER HERE
"""
from SearchStructures import Stack, Queue
from Maze import Maze

class MazeSolver:
    # Constructor
    # Inputs:
    #   maze: The maze to solve (Maze)
    #   searchStructure: The search structure class to use (Stack or Queue)
    def __init__(self, maze, searchStructure):
        self.maze = maze             # The maze to solve
        self.ss = searchStructure()  # Initialize a searchStructure object

    def tileIsVisitable(self, row:int, col:int) -> bool:
        #check if out of bounds,
        if row >= self.maze.num_rows or row < 0:
            #print("out of range")
            return False
        elif col >= self.maze.num_cols or col < 0:
           # print("out of range")
            return False
        elif self.maze.contents[row][col].visited() == True:
            #print("already visited")
            return False
        elif self.maze.contents[row][col].isWall() == True:
            #print("is wall")
            return False
        else: 
            #print("can visit")
            return True

    def solve(self):
        
        self.ss.add(self.maze.start)
        
        while not self.ss.isEmpty():
            
            current = self.ss.current()
            
            self.maze.contents[current.getRow()][current.getCol()].visit()
            self.ss.remove()

            if current == self.maze.goal:
                return 
            else: 
                if (self.tileIsVisitable(current.getRow() - 1, current.getCol())):
                    self.maze.contents[current.getRow() - 1][current.getCol()].setPrevious(current)
                    self.ss.add(self.maze.contents[current.getRow() - 1][current.getCol()])

                if (self.tileIsVisitable(current.getRow() + 1, current.getCol())):
                    self.maze.contents[current.getRow() + 1][current.getCol()].setPrevious(current)
                    self.ss.add(self.maze.contents[current.getRow() + 1][current.getCol()])

                if (self.tileIsVisitable(current.getRow(), current.getCol() + 1)):
                    self.maze.contents[current.getRow()][current.getCol() + 1].setPrevious(current)
                    self.ss.add(self.maze.contents[current.getRow()][current.getCol() + 1])

                if (self.tileIsVisitable(current.getRow(), current.getCol() - 1)):
                    self.maze.contents[current.getRow()][current.getCol() - 1].setPrevious(current)
                    self.ss.add(self.maze.contents[current.getRow()][current.getCol() - 1])
        return None

    def getPath(self):
        array = []
        goalX = self.maze.goal.getRow()
        goalY = self.maze.goal.getCol()
        current = self.maze.contents[goalX][goalY]

        while (current != None):
            array.insert(0,current)
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
    maze = Maze(["____",
                 "S##G",
                 "__#_",
                 "____"])
    # Initialize the MazeSolver to be solved with a Stack
    solver = MazeSolver(maze, Stack)

    solver.solve()
    # Print the solution found
    solver.printSolution()