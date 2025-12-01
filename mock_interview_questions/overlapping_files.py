# Question:
# We are working on a program that downloads a large file. It downloads the file in chunks. 
# The chunks can be written as `[start, end)`. 
# These chunks can:
    # - start and end at any byte
    # - overlap with each other

# Test Cases:
# 1. Valid Out of Order Case with Overlap: 
#    File size = 10, chunks = [[4,6),[0,5), [5,10)] -> True 0->9
# 2. Invalid Out of Order Case with Overlap: 
#    File size = 10, chunks = [[4,6),[0,5), [5,11)] -> False (chunks are too big)
# 3. Valid In Order Case with Overlap:
#    File size = 10, chunks = [[0,6),[2,5), [5,10)] -> True 0->9
# 4. Invalid In Order Case with Overlap:
#    File size = 10, chunks = [[0,6),[2,5), [5,9)] -> False (chunks are too small)
# 5. Valid In Order Case without Overlap:
#    File size = 10, chunks = [[0,3),[3,5), [5,10)] -> True 0->9
# 6. Valid Out of Order Case without Overlap:
#    File size = 10, chunks = [[4,6),[0,4), [6,10)] -> True 0->9

from typing import List
import heapq

# Part 1:

# Runtime: O(n logn) where n is the length of chunks list (n logn due to sorting)
# Space: O(1) just to store counter variable, sorting is done inplace 
def is_file_done(chunks: List[List[int]], file_size: int) -> bool:
    counter = -1
    chunks.sort()
    for chunk in chunks:
        start = chunk[0]
        end   = chunk[1]
        if (start - 1) == counter or start <= counter < end:
            counter = end - 1
    if (counter + 1) == file_size:
        return True
    else:
        return False

# Part 2:

# Solution 1:
class FileDownloader:
    def __init__(self, size: int) -> None:
      self.file_size = size
      self.chunks = []
    
    # Runtime: O(1) constant time to append to a list
    # could potentially move sorting here but it wouldn't impact overall runtime of 
    # the class, this function would be O(nlogn) and is_file_done would be O(n)
    def add_chunk(self, start:int, end:int) -> None:
        self.chunks.append([start,end])

    # use file size as global variable
    # Runtime: O(n logn) where n is the length of chunks list (n logn due to sorting)
    # Space: O(n) chunks is being stored globally where n is the length of the chunks
    def is_file_done(self) -> bool:
        counter = -1
        self.chunks.sort()
        for chunk in self.chunks:
            start = chunk[0]
            end   = chunk[1]
            if (start - 1) == counter or start <= counter < end:
                counter = end - 1
        if (counter + 1) == self.file_size:
            return True
        else:
            return False

# Solution 2:

# another possible solution could be to precompute the values, eliminate sorting
# have a global hashmap the size of the file
# everytime you add a new chunk you check the keys and add a new value if it doesn't exist, O(1) for lookup and insertion
# then in is_file_done you can just compare hashmap size to file_size if equal return true if not return false

# Questions:
# can the chunks added be invalid(eg. out of range of the file_size?)

# Space: O(n) where n is the size of the file (for hashmap)
class FileDownloader:
    def __init__(self, size: int) -> None:
      self.file_size = size
      self.processed_chunks = {}
    
    # Runtime: O(n) where n is the size of the chunk, worst case it's the file size
    def add_chunk(self, start:int, end:int) -> None:
        # range is inclusive of start and exclusive of end
        if start > self.file_size and end > self.file_size:
            return
        for i in range(start, end):
            if self.processed_chunks.get(i) is None:
                self.processed_chunks[i] = True

    # Runtime: O(1)
    def is_file_done(self) -> bool:
        if (len(self.processed_chunks) + 1) == self.file_size:
            return True
        else:
            return False   

# Solution 3:
# - use heap during add_chunk question
#     - push on to heap every chunk
# - in is_file_done
#     - wait till the top of heap is the first chunk
#     - then pop it and updated global counter
#     - keep waiting till you get consecutive chunks and increment your counter
#     - return when counter = file size
# - worst case heap will take O(n) space where n is the number of chunks (file size or greater)
# - average case it will be smaller and not take as much space
# - pop as you process chunks (don’t need to store all of them)

class FileDownloader:
    def __init__(self, size: int) -> None:
      self.file_size = size
      self.heap = []
      self.counter = 0
    
    # Runtime: O(logn) where n is the number of chunks
    def add_chunk(self, start:int, end:int) -> None:
        # range is inclusive of start and exclusive of end
        if start >= self.file_size and end > self.file_size:
            return
        heapq.heappush(self.heap, (start,end))

    # Runtime: O(n logn) where n is the number of chunks
    def is_file_done(self) -> bool:
        while self.heap:
            start, end = heapq.heappop(self.heap)
            if start <= self.counter < end:
                self.counter = end - 1
            else:
                break
        if self.counter == self.file_size:
            return True
        else:
            return False  