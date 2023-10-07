"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

https://leetcode.com/problems/two-sum/
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # only one solution

        # naiive appraoch
        #         for i, a in enumerate(nums):
        #             for j, b in enumerate(nums):
        #                 if i==j: continue

        #                 if (a+b == target):
        #                     return [i, j]

        # second attempt
        h = {}
        for i, num in enumerate(nums):
            # compute an expression.
            # save one half of the expression for later lookup
            n = target - num
            # what to do with b? save it. but why?
            if n not in h:
                # this means it's the first time we created this entry
                h[num] = i
            else:
                # we have found another entry in h that was created by a num
                # which means target - num_0 == target - num_1
                # we already saved the result of (target - num_0) in a hash table
                # this time, we have found the result (taget - num_1)
                return [h[n], i]
