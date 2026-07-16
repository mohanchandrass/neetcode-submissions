import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for w in stones:
            heapq.heappush(heap,-w)
        
        while len(heap)>1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if(x<y):
                heapq.heappush(heap,-(y-x))
            else:
                heapq.heappush(heap,-(x-y))
            
        return -heap[0]
            


    
            


        