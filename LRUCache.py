# Wasn't able to fully solve the question, fails for larger test cases
# get() and put() dont run in O(1) time

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # initializing Cache Data Structures
        self.capacity = capacity
        self.map = {}
        self.queue = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        # Case when the key doesn't exist
        if self.map.get(key) is None:
            return -1

        # Case where the key exists
        else:
            # Loop through queue and remove key then add it back to end of queue (LRU)
            for i in range(0, len(self.queue)):
                if self.queue[i] == key:
                    self.queue.pop(i)
                    break
            self.queue.append(key)
            return self.map.get(key)
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # Case where the map is full (length of the map is equal to capacity)
        if len(self.map) == self.capacity:
            # Case where key doesn't already exist 
            if self.map.get(key) is None:
                # Remove least used item (front of queue) from queue and map, add new value
                item = self.queue.pop(0)
                print(item)
                self.map.pop(item)
                self.map[key] = value
                self.queue.append(key)
            # Case where key exists and just need to update value
            else:
                # Loop through queue and remove key then add it back to end of queue (LRU)
                for i in range(0, len(self.queue)):
                    if self.queue[i] is key:
                        self.queue.pop(i)
                        break
                self.queue.append(key)
                self.map[key] = value
        else:
            # Loop through queue and remove key then add it back to end of queue (LRU)
            for i in range(0, len(self.queue)):
                if self.queue[i] is key:
                    self.queue.pop(i)
                    break
            self.queue.append(key)
            self.map[key] = value
