class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        merged = [intervals[0]]
        for start,end in intervals[1:]:
            merged_end = merged[-1][1]
            if start<=merged_end:
                merged[-1][1] = max(merged_end,end)
            else:
                merged.append([start,end])
        
        return merged
        