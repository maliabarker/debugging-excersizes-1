"""
Exercise 2
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# - What error message (if any) is there?
# - What line number is causing the error?
# - What can you deduce about the cause of the error?

'''
The second test case (input: [4, 1, 2, 3]) is expected to return True, but it is returning False
'''

# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!

'''
It seems we are trying to check each number against eachother in one if statement, but it does not loop through entirely before returning.
I assume the issue is in this if and return statement.
If the first loop does not pass the test, it will automatically return false and we do not continue through the list. We need to check the entire list before returning.
Let's first print the values of each checked number to see if it continues through the entire list or not.
With these print statements, we can see that it goes through the first loop and then exits. We would have to add a catch here to continue.

To solve: Only return true if the test passes. Have no else false statement, instead if loop finishes and there is no true statement, then return false once it breaks out of loop
'''

def contains_3_consecutive(list_of_nums):
    """Return True if the list contains 3 consecutive numbers each increasing by 1."""
    for i in range(len(list_of_nums) - 2):
        print(f'First number: {list_of_nums[i]}')
        print(f'Second number: {list_of_nums[i+1]}')
        print(f'Third number: {list_of_nums[i+2]}')

        if (list_of_nums[i+1] == list_of_nums[i] + 1 and
            list_of_nums[i+2] == list_of_nums[i] + 2):
            return True

        # To solve: delete this else statement
        # else:
        #     return False

    return False

if __name__ == '__main__':
    print('### Problem 2 ###')
    answer1 = contains_3_consecutive([1, 2, 4])
    print(answer1) # should print False

    answer2 = contains_3_consecutive([4, 1, 2, 3])
    print(answer2) # should print True