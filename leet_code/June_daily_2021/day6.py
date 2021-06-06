from sortedcontainers import SortedDict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = SortedDict()
        max_c = 0
        curr_c = 0
        prev_c = -2
        
        for num in nums:
            d[num] = True
        
        for val in d:
            if val == prev_c+1:
                curr_c += 1
            else:
                max_c = max(curr_c, max_c)
                curr_c = 1
            prev_c = val
        
        max_c = max(curr_c, max_c)
                
        return max_c