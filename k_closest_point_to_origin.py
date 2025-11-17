# https://neetcode.io/problems/k-closest-points-to-origin?list=neetcode150



import math
import heapq
from typing import List

# Iteration 1
# Runtime and Space Complexity:
# Runtime: O(n) where n is the length of the points array
# Space: O(n) where n is the length of the points array
class Solution:
    def k_closest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [0 for i in range(len(points))]
        hash_map = {}

        for i, point in enumerate(points):
            total = point[0]**2 + point[1]**2
            dist = math.sqrt(total)
            distances[i] = -dist

            if hash_map.get(dist):
                hash_map[dist].append(point)
            else:
                hash_map[dist] = [point]
        
        print(hash_map)
        heapq.heapify(distances)

        while len(distances) > k:
            heapq.heappop(distances)

        result = []
        for i in range(k):
            key = heapq.heappop(distances)
            values = hash_map.get(abs(key))
            if values:
                result.append(values.pop())

        return result

# Iteration 2
# Runtime and Space Complexity:
# Runtime: O(n) where n is the length of the points array
# Space: O(n) where n is the length of the points array
class Solution:
    def k_closest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for x,y in points:
            dist = math.sqrt((x**2) + (y**2))
            min_heap.append([dist,x,y])
     
        heapq.heapify(min_heap)
        result = []

        while k > 0:
            dist, x, y = heapq.heappop(min_heap)
            result.append([x,y])
            k -= 1

        return result