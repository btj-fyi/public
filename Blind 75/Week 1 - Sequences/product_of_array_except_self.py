"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

# NOTES
# could easily brute force it with nested for loops but we don't
# want to do that. I accidentally read this as sum the at first glance
# but now see it says product. if we could use division it is always
# the product divided by value of nums[i] but we aren't allowed division
# and we would have to check for division by zero too in that case
# some observations:
# - our answer and inputs lists will be of the same length
# - if we have any zeros the whole thing will be zero anywhere we haven't
# excluded zero. so if we have two zeros the thing is always a list of zeros
# - if we have a one removing it doesn't change the product

# what if we came at it from both directions?
nums: list[int] = [1, 2, 3, 4]


def ProductOfArrayExceptSelf(nums: list[int]) -> list:
    skip_i = 0
    i = 0
    answer = []
    count = 0
    while True:
        if count < len(nums):
            if i < len(nums):
                if i != skip_i:
                    print("a")
                    answer[skip_i] *= nums[i]
                    i += 1
                else:
                    print("b")
                    answer.insert(skip_i, 1)
                    i += 1
            else:
                print("c")
                count += 1
                skip_i += 1
                answer.insert(skip_i, 1)
                i = 0
        else:
            print("d")
            break
    return answer


print(ProductOfArrayExceptSelf(nums))

# SOLUTION
# find prefix and suffix
# I don't really understand how the two loops are excluding the numbers at each index


def Solution(nums: list[int]) -> list[int]:
    n = len(nums)
    pre = 1
    suf = 1
    result = [0] * n
    for i in range(n):
        result[i] = pre
        pre *= nums[i]

    for i in range(n - 1, -1, -1):
        result[i] *= suf
        suf *= nums[i]
    return result


print(Solution(nums))
