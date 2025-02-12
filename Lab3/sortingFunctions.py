"""
Name: Jose Torres
File Name: sortingFunctions.py
Description: Implementation of sorting algorithms.
"""

import time, random

# Implementation of insertionSort algorithm - swapping elements
def insertionSort(list_to_sort: list) -> list:
    #Loop array
    for index in range(len(list_to_sort)):
        j = index
        #checek j in bounds and the previous element is smaller than currrent
        while j > 0 and list_to_sort[j-1] > list_to_sort[j]: 
            swap(list_to_sort, j, j-1)
            j-=1
    return list_to_sort

# Second Implementation of insertion sort using shift
def insertionSort_1(list_to_sort: list) -> list:
    for index in range(1, len(list_to_sort)): #Start at 1 since first element is always in "Correct Place"
        value = list_to_sort[index] #Store the value of current element
        j = index - 1 #Store the previous element
        while (value < list_to_sort[j] and j >= 0):
            list_to_sort[j+1] = list_to_sort[j] #Shift elements to the right
            j = j - 1 #Decrement j to check values more left
        list_to_sort[j+1] = value #Once you have shifted all the way insert the value back
    return list_to_sort

# Implementation of bubbleSort algorithm
def bubbleSort(list_to_sort:list) -> list:
    for i in range(len(list_to_sort) - 1):
        for j in range(len(list_to_sort) - 1 - i): #Decrement range every time previous loop increments
            if list_to_sort[j] > list_to_sort[j + 1]:
                swap(list_to_sort,j, j+1)
    return list_to_sort

def swap(a,j,i):
    temp = a[j]
    a[j] = a[i]
    a[i] = temp

def merge(left_array: list, right_array: list):
    array = []
    i = 0
    j = 0

    L = len(left_array)
    R = len(right_array)

    while (i < L and j < R):
        if left_array[i] <= right_array[j]:
            array.append(left_array[i])
            i+=1
        else:
            array.append(right_array[j])
            j+=1

    while (i < L):
        array.append(left_array[i])
        i+=1
    
    while (j < R):
        array.append(right_array[j])
        j+=1
  
    return array

def mergeSort(array: list):
    if len(array) < 2:
        return array

    left_array = array[:len(array)//2]
    right_array = array[len(array)//2:]
    #mergeSortLeft
    left_array = mergeSort(left_array)
    #mergeSortRight
    right_array = mergeSort(right_array)

    return merge(left_array,right_array)
    #mergeBothArray

def partition(A: list, start, end):
    pivot = A[end]
    pIndex = 0

    for index in range(end):
        if A[index] <= pivot:
            A[index], A[pIndex] = A[pIndex], A[index]
            pIndex+=1
    
    A[pIndex], A[end] = A[end], A[pIndex]

    return pIndex

def quickSort(A, start, end):
    if start >= end:
        return A
   
    index = partition(A, start, end)

    quickSort(A, start, index - 1)
    quickSort(A, index + 1, end)

    return A
  
# Returns a random list of the given length
def createRandomList(length:int) -> list:
    return random.sample(range(max(100, length)), length)
    
# Returns the length of time (in seconds) that it took
# for the function_to_run to sort a list of length list_length
def getRuntime(function_to_run, list_length) -> float:
    # Create a new list to sort
    list_to_sort = createRandomList(list_length)
    # Get the time before running
    start_time = time.time()
    # Sort the given list
    function_to_run(list_to_sort)
    # Get the time after running
    end_time = time.time()
    # Return the difference
    return end_time - start_time

def test(A):
    A = []
    print("in test: ", A)

if __name__ == '__main__':
    A = [2,1,7,9,4]
    print(A)
    print(insertionSort(A))

pass