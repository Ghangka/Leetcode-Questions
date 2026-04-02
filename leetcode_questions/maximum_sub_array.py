# https://neetcode.io/problems/maximum-subarray/question?list=blind75

from typing import List

# Runtime: O(n)
# Space: O(1)

# Kadane's Algorithm

class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        maxSub, curSum = nums[0], 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub