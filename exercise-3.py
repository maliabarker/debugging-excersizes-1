"""
Exercise 3
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# - What error message (if any) is there?
# - What line number is causing the error?
# - What can you deduce about the cause of the error?

'''
We get the Traceback error printed in the terminal:

Traceback (most recent call last):
  File "/Users/maliabarker/Desktop/main/MakeSchool/Term8/SPD_2.3/SPD-2.3-Debugging-Steps-Lab/exercise-3.py", line 34, in <module>
    answer = insertion_sort([5, 2, 3, 1, 6])
  File "/Users/maliabarker/Desktop/main/MakeSchool/Term8/SPD_2.3/SPD-2.3-Debugging-Steps-Lab/exercise-3.py", line 26, in insertion_sort
    while key < arr[j] : 
IndexError: list index out of range

The error is coming from line 26, inside the insertion_sort function.

The error states the list index is out of range, so we assume j exceeds the length of the list.

Our expected output is a sorted list of numbers.
'''

# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.

'''
We assume the loop starts at index 1 (skips first num in array) and continues until the end of the array.

We assume that arr[j] is the 'first' number to compare to the key, or the 'second' number.

In the while loop, we assume it continues until the number in position of j is less than the number we are comparing (key)

We assume that is the current previous number is great than the following number, we 
'''

def insertion_sort(arr):
    """Performs an Insertion Sort on the array arr."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        # We assume the loop starts at index 1 (skips first num in array) and continues until the end of the array, and nothing exceeds this limit.
        # We assume that arr[j] is the 'first' number to compare to the key, or the 'second' number, so the index of key is always initially greater than the index of j.
        
        print(f'Length of arr: {len(arr)}')
        print(f'J: index = {j} value = {arr[j]}')
        print(f'KEY: index = {i} value = {key}')

        print('\nWHILE LOOP START')
        while key < arr[j] and j>=0:
            # We assume j is an acceptable index in the list 
            print(f'J index {j} (value of {arr[j]}) is within limits of {range(len(arr))}: {j in range(len(arr))}')

            # In the while loop, we assume it continues until the number in position of j is less than the number we are comparing (key)
            print(f'Key ({key}) is less than J position ({arr[j]}): {key < arr[j]}')

            # We assume J is still in the index range of the list
            print(f'J index ({j}) and proceeding index ({j+1}) will not exceed list length of {len(arr) - 1}')

            # We assume j and its proceeding number will be swapped, or we move the proceding number back
            print(f'Swapping proceeding num ({arr[j+1]}) with current num ({arr[j]})')
            arr[j+1] = arr[j]
            print(f'Current Array {arr}')

            # We assume that j decreases by 1
            j -= 1
            print(f'New j value {j}')

            print('———————————————')

        print('\nWHILE LOOP BROKEN')
        # We assume that once the while loop is broken, the key will be greater than the num in j position
        print(f'Key ({key}) is greater than J position ({arr[j]}): {key > arr[j]}')

        # We assume the proceeding value of the j position we ended at is replaced with the key value
        arr[j+1] = key
        print(f'Sorted Array: {arr}\n\n')

    return arr


if __name__ == '__main__':
    print('### Problem 3 ###')
    answer = insertion_sort([5, 2, 3, 1, 6])
    print(answer)

