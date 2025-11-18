# https://neetcode.io/problems/kth-largest-element-in-an-array?list=neetcode150 
# Runtime & Space Complexity:
# Runtime: O(n log n)
# Space: O(n)

import heapq
from typing import List

class Solution:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]