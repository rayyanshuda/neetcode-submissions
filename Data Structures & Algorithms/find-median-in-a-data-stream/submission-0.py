class MedianFinder:

    def __init__(self):
        # max-heap so top element is middle number
        self.small = []
        # min-heap so top element is middle number
        self.large = []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        if self.large and -self.small[0] > self.large[0]:
            largest = -heapq.heappop(self.small)
            heapq.heappush(self.large, largest)
        
        if len(self.small) > len(self.large) + 1:
            top = -heapq.heappop(self.small)
            heapq.heappush(self.large, top)
        
        elif len(self.large) > len(self.small):
            top = heapq.heappop(self.large)
            heapq.heappush(self.small, -top)

    def findMedian(self) -> float:
        # odd number of total elements -> top of max-heap
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
    
        # eve number of total elements -> average of both tops
        return (-1 * self.small[0] + self.large[0]) / 2.0
        
        