"""
Exercise 1
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# - What error message (if any) is there?
# - What line number is causing the error?
# - What can you deduce about the cause of the error?

'''
This is the Traceback printed in terminal

Traceback (most recent call last):
  File "/Users/maliabarker/Desktop/main/MakeSchool/Term8/SPD_2.3/SPD-2.3-Debugging-Steps-Lab/exercise-1.py", line 31, in <module>
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])
  File "/Users/maliabarker/Desktop/main/MakeSchool/Term8/SPD_2.3/SPD-2.3-Debugging-Steps-Lab/exercise-1.py", line 23, in find_largest_diff
    diff = abs(list_of_nums[i] - list_of_nums[i+1])
IndexError: list index out of range

The error seems to originate from line 23 in the find_largest_diff function. 
The error states that list index in out of range. 
'''


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
'''
We assume i will be a number index that exists in the list given, obviously this exceeds the length of the list.
We also assume, in conjunction with the one above, that i+1 will not exceed the list.
If there is always an i+1, and we only need the difference of consecutive numbers (meaning we do not have to add the last number in list with first number), then we need to make sure that i+1 never exceeds the length of the list.
To make sure that i+1 doesn't exceed the length of the list, we need to first check what i is and then make sure our range declared in the for loop is limited.

To fix: To make sure i+1 does not exceed the list length, just subtract 1 from the length of the list (before wrapping in range parentheses)
'''

def find_largest_diff(list_of_nums):
    """Find the largest difference between *consecutive* numbers in a list."""
    largest_diff = 0
    for i in range(len(list_of_nums)-1):
        print(f'First index: {i}')
        print(f'Second index: {i+1}')
        print(f'Length of list: {len(list_of_nums)}')
        if i+1 >= len(list_of_nums):
            print('ERROR: i exceeds list length')

        diff = abs(list_of_nums[i] - list_of_nums[i+1])
        if diff > largest_diff:
            largest_diff = diff

    return largest_diff

if __name__ == '__main__':
    print('### Problem 1 ###')
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])

    # This should print 4, as the largest diff between consecutive numbers is between 2 and 6
    print(answer)