# Class Type Question
# Runtime is O(1) average or of O(N) worst case when hashmap needs to find last item that was added to the map

class IdAllocator:
    def __init__(self):
        self.counter = 0
        self.idMap = {}
    
    def alloc(self) -> int:
    # check if the hashmap is not empty O(1)
    # if not empty then use a for loop to loop through only the first element O(1) time
    # remove that element from the hashmap and return that element
        if len(self.idMap) > 0:
            # pops item that was last put on the hashmap
            item = self.idMap.popitem()
            return item[0]
    # if hashmap is empty, then increment counter and return new value
        else:
            self.counter += 1
            return self.counter

    def release(self, id: int) -> None:
    # check if the id is valid
    # make sure the id is smaller or equal to the global counter O(1)
    # check if the id exists on the hashmap, if it does the id has already been released O(1)
        if (id <= self.counter) and (self.idMap.get(id) is None):
            # if not add the id to hashmap O(1)
            self.idMap[id] = True
        else:
            raise Exception("This id doesn't exist or has already been released.")

# Test Cases:

# Allocates and Releases Successfully
# ids = IdAllocator()
# print(ids.alloc())
# print(ids.alloc())
# print(ids.alloc())
# ids.release(1)
# ids.release(2)
# ids.release(3)

# Throws error when trying to release and id that doesn't exist
# ids2 = IdAllocator()
# ids2.release(1)

# Allocates and Releases Successfully
ids3 = IdAllocator()
one = ids3.alloc()
print(one)
two = ids3.alloc()
print(two)
ids3.release(one)
three = ids3.alloc()
# should print 1
print(three)

