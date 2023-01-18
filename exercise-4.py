"""
Exercise 4
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# - What error message (if any) is there?
# - What line number is causing the error?
# - What can you deduce about the cause of the error?

'''
This is the Traceback error printed in the terminal

Traceback (most recent call last):
  File "/Users/maliabarker/Desktop/main/MakeSchool/Term8/SPD_2.3/SPD-2.3-Debugging-Steps-Lab/exercise-4.py", line 41, in <module>
    answer = binary_search([1, 2, 4, 5, 7], 7)
  File "/Users/maliabarker/Desktop/main/MakeSchool/Term8/SPD_2.3/SPD-2.3-Debugging-Steps-Lab/exercise-4.py", line 37, in binary_search
    return binary_search(arr, element, mid, high)
  File "/Users/maliabarker/Desktop/main/MakeSchool/Term8/SPD_2.3/SPD-2.3-Debugging-Steps-Lab/exercise-4.py", line 37, in binary_search
    return binary_search(arr, element, mid, high)
  File "/Users/maliabarker/Desktop/main/MakeSchool/Term8/SPD_2.3/SPD-2.3-Debugging-Steps-Lab/exercise-4.py", line 37, in binary_search
    return binary_search(arr, element, mid, high)
  [Previous line repeated 995 more times]
  File "/Users/maliabarker/Desktop/main/MakeSchool/Term8/SPD_2.3/SPD-2.3-Debugging-Steps-Lab/exercise-4.py", line 22, in binary_search
    if high == None:
RecursionError: maximum recursion depth exceeded in comparison

This looks like a infinite loop error possibly if a maximum recursion depth is reached (assuming this is not part of the intended functionality)

A check seems to be going wrong here and not breaking the loop.

With the print statements, we can see it gets stuck
'''

# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.

def binary_search(arr, element, low=0, high=None):
    """Returns the index of the given element within the array by performing a binary search."""
    
    # we assume to start that the given list is sorted
    if high == None:
        # we assume high is equal to none here
        print(f'Value of high {high}')
        high = len(arr) - 1

        # then we assume that we assign high to the largest index value in the list
        print(f'New high val: {high}')

    if high < low:
        return -1

    mid = (high + low) // 2
    # we assume mid is the middle value, and it is an integer that is also an index value
    print(f'mid: {high} + {low} = {high+low} // 2 = {(high+low) // 2}')
    print(f'Mid index {mid}')

    if arr[mid] == element:
        # we assume that is the object at the middle
        # we assume that if this middle element is the target element, we break the function and return the element
        print(f'Element found!')
        return mid

    elif arr[mid] > element:
        # we assume the mid object is greater than the element, so we complete a new binary search between 0 and the mid
        # to solve, we need to make sure the index actually moves, so if it is greater than, we would move to the left (-1)
        print(F'Mid greater than element: {arr[mid] > element}')
        print(f'New binary search between indexes {low} and {mid}')
        return binary_search(arr, element, low, mid - 1)

    else:
        # we assume this last else statement is if mid is less than the element, new search between mid and high
        # this is where it gets stuck, it is not moving 
        # to solve, we need to make sure the index actually moves, so if it is less than, we would move to the right (+1)
        print(f'Mid less than element: {arr[mid] < element}')
        print(f'New binary search between indexes {mid} and {high}')
        return binary_search(arr, element, mid + 1, high)


if __name__ == '__main__':
    answer = binary_search([1, 2, 4, 5, 7], 7)
    print(answer)