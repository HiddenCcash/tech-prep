class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Third Attemp
        #         start = 0
        #         end = 1
        #         max_sum = 0

        #         while(start < len(nums)):

        #             curr_sum += nums[start]

        #             if (curr_sum > max_sum):

        #             max_sum = max(curr_sum, max_sum)

        #             if curr

        #             start +=1

        # First Attempt
        #         i = 0

        #         if len(nums) == 1:
        #             return nums[0]
        #         j = 1

        #         best_sum = nums[i] + nums[j]
        #         bests = [i, j]
        #         while((i < len(nums) -1) and (j < len(nums)-1)):
        #             if nums[i] + nums[j] > best_sum:
        #                 best_sum = nums[i] + nums[j]
        #                 bests = [i, j]
        #             else:
        #                 i += 1
        #             j += 1
        #         return sum(nums[bests[0]:bests[1]])

        # Second Attempt
        i = 0
        j = 1
        if len(nums) == 1:
            return nums[0]
        best_sum = nums[i] + nums[j]
        bests = [0, 1]

        while((i < len(nums)) and (j <= len(nums))):
            if nums[i] + nums[j] > best_sum:
                bests = [i, j]
            else:
                i += 1
            j += 1
        # print(nums[bests[0]:bests[1]+1])
        return sum(nums[bests[0]:bests[1]+1])

        # Incorrect
#         # pair the index and value together
#         index_arr = [(i, val) for i, val in enumerate(nums)]

#         # sort based on val
#         sort_arr = sorted(index_arr, key=lambda x: x[1], reverse=True)

#         # [(3, 4), (8, 4), (5, 2), (1, 1), (6, 1), (4, -1), (0, -2), (2, -3), (7, -5)]

#         i = 0
#         j = 1
#         prev_sum = sort_arr[-1][1] # first store lowest number as the highest summation
#         best_nums = sort_arr[i:j]
#         while(i < len(nums)):
#             print(i, j)
#             _sum = sort_arr[i][1] + sort_arr[j][1]

#             if _sum > prev_sum:
#                 j += 1
#                 best_nums = sort_arr[i:j]
#             else:
#                 i += 1

#         return [x[0] for x in sorted(best_nums, key=lambda x: x[1])]

#         # check if _sum is greater than previous saved _sum, or if i has reached n-1
