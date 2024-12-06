from heapq import heapify, heappop, heappush,heapreplace
from typing import List
class KthLargest:
   
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapify(self.heap)
        self.k = k  
        while len(self.heap) > k:
            heappop(self.heap)
    
    def add(self, val: int) -> int:
        if len(self.heap) > self.heap[0]:
            heapreplace(self.heap,val)
        return self.heap[0] 
