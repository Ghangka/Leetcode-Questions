# https://neetcode.io/problems/find-median-in-a-data-stream/question?list=blind75

import math
import heapq

# Solution 1: Sorting
class MedianFinder:

    def __init__(self):
        self.nums = []
        self.median = 0
        
    # Runtime: O(nlogn)
    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

        if len(self.nums) % 2 == 0:
            median_1 = math.floor(len(self.nums)/2)
            median_2 = median_1 - 1
            
            self.median = (self.nums[median_1] + self.nums[median_2])/2
        else:
            self.median = self.nums[math.floor(len(self.nums)/2)]
    
    # Runtime: O(1)
    def findMedian(self) -> float:
        return self.median

# Solution 2: Heap
class MedianFinder2:

    def __init__(self):
        self.min_nums = []
        self.max_nums = []
    
    # Runtime: O(logn)
    def addNum(self, num: int) -> None:
        if len(self.min_nums) == 0 and len(self.max_nums) == 0:
            heapq.heappush(self.max_nums, num)
        
        elif num > self.max_nums[0]:
            heapq.heappush(self.max_nums, num)
        else:
            heapq.heappush(self.min_nums, -1 * num)

        while abs(len(self.min_nums) - len(self.max_nums)) > 1:
            if len(self.min_nums) > len(self.max_nums):
                heapq.heappush(self.max_nums, -1*heapq.heappop(self.min_nums))
            else:
                heapq.heappush(self.min_nums, -1* heapq.heappop(self.max_nums))

    # Runtime: O(1)
    def findMedian(self) -> float:
        if len(self.min_nums) > len(self.max_nums):
            return -1* self.min_nums[0]
        elif len(self.max_nums) > len(self.min_nums):
            return self.max_nums[0]
        else:
            return (-1 * self.min_nums[0] + self.max_nums[0])/2.0
        