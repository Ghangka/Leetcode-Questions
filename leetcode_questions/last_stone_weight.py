# https://neetcode.io/problems/last-stone-weight?list=neetcode150

# Runtime: O(nlogn) where n is the length of stones
# Space: O(n) where n is the length of stones

from ast import List
import heapq


class Solution:
    def last_stone_weight(self, stones: List[int]) -> int:
        # Negate all stones to simulate a max-heap
        max_heap = [-s for s in stones]
        
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)

            if x == y:
                continue
            stone = x - y
            heapq.heappush(max_heap,stone)
        
        return abs(heapq.heappop(max_heap)) if max_heap else 0