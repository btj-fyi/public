"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

"""
import time

numbers: list = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]


def contains_duplicates(numebrs: list) -> bool:
    numbers_set = set(numbers)
    if len(numbers) != len(numbers_set):
        return True
    else:
        return False


# REVIEW
# this question took me 3.5min w/o any reources
# I believe this solution is actually acceptable

# SOLUTION
# apparently a better solution is to do almost exactly as two_sum
# that is traverse the array, add each value to a dict as you traverse the list
# then check if the next value exists as a key in the dict
# if yes, true
# if not, and end of list, false
# I am going to test to see if this is actually a more performant method

start = time.time()


def Solution(numbers: list) -> bool:
    hashmap: dict = {}
    for number in numbers:
        if number in hashmap:
            return True
        else:
            hashmap[number] = numbers.index(number)
    return False


start = time.time()
print(contains_duplicates(numbers))
end = time.time()
print(f"Time Taken: {(end-start)*10**3:.03f}ms")

start = time.time()
print(Solution(numbers))
end = time.time()
print(f"Time Taken: {(end-start)*10**3:.03f}ms")


# sooo they're the same.... lol that was a waste of effort to test.
