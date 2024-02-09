"""
Given an integer array nums, find the 
subarray with the largest sum, and return its sum.
"""

nums: list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums1: list = [1]
nums2: list = [5, 4, -1, 7, 8]


def MaximumSubarray(nums: list) -> int:
    return


# SOLUTION
# I was not able to do this one without looking at the solutions. There are many
# ways to solve this problem. The solution that I investiaged more closely was
# Kadane's Algorithm - if the number at our current index is greater than or
# equalt to the sum of the previous numbers plus itself, we are better off continuing our
# subarray from the number at our current index. Each time we calculate a
# maximum between the number at the current index and the previous numbers plus itself
# we should compare to our previous greatest maximum - if it is greater, replace it.


# When the combination of the previous numbers plus the current number is greater than the
# current number, it is better to start with the combination of the previous numbers plus the
# current number. However, when the current number is greater than the combination of the previous
# numbers plus the current number, it is better to start with the current number.

# This is because the sum of the subarray preceding the current number is lower than the current
# number and will only diminish the possibly greater sum of the next subarray in the array. In the event
# the array does not contain a subarray of a greater sum, it is important that we greatest subarray
# sum we observe each time we observe a greater sum.


def Solution(nums: list[int]) -> int:
    cur_max: int = 0
    prev_max: int = 0
    for num in nums:
        print("index:", nums.index(num))
        print("num:", num)
        print(f"cur_max = max({num},{num} + {cur_max})")
        cur_max = max(num, cur_max + num)
        print(cur_max)
        print(f"prev_max =max({prev_max},{cur_max})")
        prev_max = max(prev_max, cur_max)
        print(prev_max)
        print()
    return prev_max


print(Solution(nums))
# print(Solution(nums1))
# print(Solution(nums2))
