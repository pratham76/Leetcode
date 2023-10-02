class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #O(nlogn)
        '''
        intervals.sort(key=lambda i:i[0])
        output=[intervals[0]]
        for start,end in intervals[1:]:
            lastend=output[-1][1]
            if start<=lastend:
                output[-1][1]=max(lastend,end)
            else:
                output.append([start,end])
        return output
        '''

        intervals.sort(key=lambda i:i[0])
        output=[intervals[0]]
        for i,j in intervals[1:]:
            le=output[-1][1]
            if i<=le:
                output[-1][1]=max(le,j)
            else:
                output.append([i,j])
        return output
