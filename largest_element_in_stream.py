# https://neetcode.io/problems/kth-largest-integer-in-a-stream?list=neetcode150

# Runtime: O(mlogk)where m is the number of add() calls
# Space: O(k) 

from ast import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums
        self.k = k

        # sorts heap to make minimum value be at root node in O(n) time
        heapq.heapify(self.min_heap)
        
        while len(self.min_heap) > k:
            # pops top of the heap and then restructures heap O(log n)
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # pushes new value onto heap O(log n) - because element added could be
        # the smallest item and would need to bubble up to the top of the stack
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            # pops top of the heap and then restructures heap O(log n)
            heapq.heappop(self.min_heap)

        return self.min_heap[0] if self.min_heap else None
