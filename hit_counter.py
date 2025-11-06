# Design a hit counter to record the number of hits on a webpage for the last 5 minutes.

# Assumptions:
# 1. The timestamp is a positive integer and is always increasing
# 2. The timestamp is in seconds
# 3. The timestamp is always a valid timestamp

# Edge cases:
# 1. Can have multiple hits at one timestamp


# My First solution
# Time Complexity: O(300)
# Space Complexity: O(300)
class HitCounter1:
  def __init__(self):
    # to store timestamps of hits
    # how big should the queue be? 5 minutes * 60 seconds (a hit every second?)
    self.queue = []
  
  # push new timestamp onto queue
  def hit(self, timestamp: int) -> None: 
    if len(self.queue) == 300: 
        self.queue.pop(0) 
        self.queue.append(timestamp)
        return
    self.queue.append(timestamp) # t1, t2

  # return number of hits from the last 5 minutes to timestamp (timestamp - 5 mintues)
  # Assumption: timestamp is in seconds
  # O(n) Time 
  def get_hits(self, timestamp: int) -> int:
    start = timestamp - 300         
    end = timestamp
    counter = 0

    for time in self.queue:
        # inclusive of both start and end times
        if start <= time and time <= end:
            counter += 1
    print("solution 1 count:", counter)
    return counter


# Second Solution, takes into account multiple hits in one second
# Time Complexity: O(300)
# Space Complexity: O(600)
class HitCounter:

    def __init__(self):
        # array to store the number of hits
        self.hits = [0]*300
        self.times = [0]*300

    def hit(self, timestamp: int) -> None:
        # maps each timestamp to a number between 0-299
        index = timestamp % 300
        if self.times[index] != timestamp:
            self.times[index] = timestamp
            self.hits[index] = 1
            return
        self.hits[index] += 1
        return

    # this function can be given any timestamp and will return the number of hits in the last 5 minutes
    def get_hits(self, timestamp: int) -> int:
        count = 0
        start = timestamp - 300

        for index, time in enumerate(self.times):
            if time > start and time <= timestamp:
                count += self.hits[index]
        print("solution 2 count: ", count)
        return count

# Test Cases:
# If you change the queue lengths and time lengths in the code above to 3 instead of 300 
# you can see the difference in the 2 solutions

hit_counter = HitCounter1()
hit_counter.hit(1)
hit_counter.hit(2)
hit_counter.hit(1)
hit_counter.hit(2)
hit_counter.hit(1)
hit_counter.hit(2)
hit_counter.get_hits(2)

hit_counter = HitCounter()
hit_counter.hit(1)
hit_counter.hit(2)
hit_counter.hit(1)
hit_counter.hit(2)
hit_counter.hit(1)
hit_counter.hit(2)
hit_counter.get_hits(2)