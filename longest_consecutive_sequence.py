# https://leetcode.com/problems/longest-consecutive-sequence/
# O(n) time complexity
# O(n) space complexity

class Solution:
    def longest_consecutive_sequence(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in num_set:
                length = 1
                while (n + length) in num_set:
                    length += 1
                longest = max(longest, length)
        return longest