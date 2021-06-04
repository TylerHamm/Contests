class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]

        h_cuts = [horizontalCuts[i]-horizontalCuts[i-1] for i in range(1, len(horizontalCuts))]
        v_cuts = [verticalCuts[i]-verticalCuts[i-1] for i in range(1, len(verticalCuts))]
        
        return (max(h_cuts)*max(v_cuts)) % (10**9 + 7)