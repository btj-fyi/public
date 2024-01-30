"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


# do any two such numbers even exist in the given array?
# there will be exactly two values in our array that add up to our target
# cannot add the same element to itself


def two_sum(numbers: list, target: int) -> tuple:
    if len(numbers) == 2 and (numbers[0] + numbers[1] == target):
        indices = (1, 2)
        return indices
    for idx_x, num_x in enumerate(numbers):
        for idx_y, num_y in enumerate(numbers):
            if num_x + num_y == target:
                indices: tuple = (idx_x, idx_y)
                return indices


numbers = [2, 7, 11, 15]
target = 9

print(two_sum(numbers, target))


# if we insert our target into the list and then sort the list
# we can then drop all elements after our target value because they are already bigger than our required value


# REVIEW
# this problem took me 16:23min w/o looking at any resources
# the solution works

# SOLUTION
# a better solution would have been to traverse the array
# find the difference between our target and our current number (aka the number we would need to add to get our target)
# store this difference in another list. each time checking if we've seen it before

# key insight is the use of a dictionary or a hash table (aka assoc data structure where we can take
# advantage of constant time lookup)


def Solution(numbers: list, target: int) -> tuple:
    previous: dict = {}
    for i in range(len(numbers)):
        difference = target - numbers[i]
        if difference in previous:
            indices = (previous[difference], i)
            return indices
        else:
            previous[numbers[i]] = i


print(Solution(numbers, target))
