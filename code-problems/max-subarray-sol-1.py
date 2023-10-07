class Solution:
    def cross_sum(self, nums, left, right, p):

        if left == right:
            return nums[left]

        # LEFT
        left_subsum = float('-inf')
        curr_sum = 0
        for i in range(p, left - 1, -1):
            curr_sum += nums[i]
            left_subsum = max(left_subsum, curr_sum)

        # RIGHT
        right_subsum = float('-inf')
        curr_sum = 0
        for i in range(p + 1, right + 1):
            curr_sum += nums[i]
            right_subsum = max(right_subsum, curr_sum)

        return left_subsum + right_subsum

    def helper(self, nums, left, right):
        # if length of nums is 1, then 1 - 1 = 0 which == left so return the element
        if left == right:
            return nums[left]

        # find the middle index and truncate (so always leans toward the left if nums is even length)
        p = (left + right) // 2

        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p + 1, right)
        cross_sum = self.cross_sum(nums, left, right, p)

        return max(left_sum, right_sum, cross_sum)

    def maxSubArray(self, nums: 'List[int]') -> 'int':
        return self.helper(nums, left=0, right=len(nums) - 1)
