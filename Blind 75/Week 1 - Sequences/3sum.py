"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

# A triplet is a set of three numbers that add up to a given value.
# For example, the sum 10 can be generated from the numbers 1,6, and 3
# or from 1,5, and 4.


# SOLUTION
# had to look at the answer for this one but once I did it is very intuitive
# once the list is sorted we can move our j and k pointers up and down the
# list respectively until such a time that we either are greater than target
# or less than in which case we want to inc/drecement only the one that will bring
# our calculate sum toward our target value - this works because the array is sorted
# by least to greatest
nums = [-1, 0, 1, 2, -1, -4]


def threeSum(nums: list[int]):
    target = 0
    nums.sort()
    triplets = set()
    result = []
    for i in range(len(nums)):  # pylint: disable=C0200
        j = i + 1
        k = len(nums) - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum == target:
                triplets.add((nums[i], nums[j], nums[k]))
                j += 1
                k -= 1
            elif sum < target:
                j += 1
            else:
                k -= 1
        result = list(triplets)
    return result


print(threeSum(nums))
