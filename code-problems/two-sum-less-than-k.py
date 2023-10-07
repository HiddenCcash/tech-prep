"""
Given an array A of integers and integer K, return the maximum S such that there 
exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this 
equation, return -1.

 

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: A = [10,20,30], K = 15
Output: -1while
Explanation: 
In this case it's not possible to get a pair sum less that 15.
 

Note:

1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000
"""


class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:

        # I'm stuck
        #         s_max = 0 # TODO explain why
        #         h = {}
        #         for i, num in enumerate(A):

        #             n = K - num

        #             if n > s_max and n not in h:
        #                 h[n] = i
        #                 s_max = n

        # Another's solution
        """
        This reminds me of the DIY technique
        """
        a = sorted(A)
        i, j = 0, len(a)-1
        ans = -1
        while i < j:
            # here, instead of iterating through the problem space for index 0, to n
            # we are stepping from both ends to the middle index, one by one
            if a[i]+a[j] < K:
                # quick tip here, take the max value of the two arguments
                ans = max(ans, a[i]+a[j])
                # why incr i instead of j?
                # b/c we are under the constraint and a[i] so we can "up the anty" by
                # waging a higher number such as a[i]
                i += 1
            else:
                # otherwise we did not meet the constraint and we have to "back off"
                j -= 1
        return ans
