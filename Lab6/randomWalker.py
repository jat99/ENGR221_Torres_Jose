"""
Name: Jose Torres
File name: randomWalker.py
Description: This program replicates a random walker using a loop over recursion.
Date: 3/4/2024
"""

import random  
import time

def rs():
    """rs chooses a random step and returns it.
       Note that a call to rs() requires parentheses.
       Arguments: none at all!
    """
    return random.choice([-1, 1])

def rwpos(start, nsteps):
    """ rwpos models a random walker that
        * starts at the int argument, start
        * takes the int # of steps, nsteps

        rwpos returns the final position of the walker.
    """
    time.sleep(0.1)
    print('location is', start)
    if nsteps == 0:
        return start
    else:
        newpos = start + rs()  # take one step
        return rwpos(newpos, nsteps - 1)

def rwsteps(start, low, hi):
    """ rwsteps models a random walker which
        * is currently at start 
        * is in a walkway from low (usually 0) to hi (max location) 
          
        rwsteps returns the # of steps taken 
        when the walker reaches an edge
    """
    walkway = "_"*(hi-low)    # create a walkway of underscores
    S = (start-low)           # this is our sleepwalker's location, start-low

    walkway = walkway[:S] + "S" + walkway[S:]  # put our sleepwalker, "S", there

    walkway = " " + walkway + " "              # surround with spaces, for now...

    print(walkway, "    ", start, low, hi)     # print everything to keep track...
    time.sleep(0.05)

    if start <= low or start >= hi:            # base case: no steps if we're at an endpt
        return 0
    
    else:
        newstart = start + rs()                # takes one step, from start to newstart
        return 1 + rwsteps(newstart, low, hi)  # counts one step, recurses for the rest!

def rwstepsLoop(start, low, hi):
    steps = 0
    #To get the same behavior as the recursion we have to do almost like a do while loop, 
    #Even if the start is out of bounds we want to print out the first line.
    while (True): #Run until a case inside loop is met. 
        walkway = "_"*(hi-low)
        S = (start - low)
        walkway = walkway[:S] + "S" + walkway[S:]
        walkway = " " + walkway + " "
        print(walkway, "    ", start, low, hi)
        if start <= low or start >= hi:#Once this is true break out of the loop
           break
        start = start + rs()
        steps +=1
    return steps

if __name__ == '__main__':
    print("Steps: ", rwstepsLoop(0,0,20))