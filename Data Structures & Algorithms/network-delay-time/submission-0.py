import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = {i: [] for i in range(1,n+1)}

        for u,v,t in times:
            graph[u].append((v,t))

        def dijkstra(graph, start):
            dist = {i: float("inf") for i in graph}
            dist[start] = 0
            heap = []

            heapq.heappush(heap,(0,start))

            while heap:
                distance, node = heapq.heappop(heap)

                if distance>dist[node]:
                    continue
                
                for neighbor,weight in graph[node]:
                    ndist = distance+weight

                    if ndist < dist[neighbor]:
                        dist[neighbor] = ndist
                        heapq.heappush(heap,(ndist,neighbor))
            
            if float("inf") in dist.values():
                return -1

            time = max(dist.values())

            return time
        

        return dijkstra(graph,k)


       





                


        