# https://leetcode.com/problems/product-of-array-except-self/
# O(n) time complexity
# O(n) space complexity

import math
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        product = 1

        for num in nums:
            product = product * num

        for num in nums:
            result.append(math.floor(product / num))
        
        return result