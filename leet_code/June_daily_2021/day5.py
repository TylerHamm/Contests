from sortedcontainers import SortedList

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        modulo = 10**9 + 7

        employees = sorted(list(zip(efficiency, speed)), reverse = True)
        
        best_l = []
        best = SortedList([])
        max_sum = 0
        
        # Get best speeds up to k-1 amounts
        for e, s in employees:
            best.add(s)
            max_sum += s
            
            #remove lowest of the group
            if len(best) > k - 1:
                max_sum -= best.pop(0)
                # m = min(best)
                # best.remove(m)
                # max_sum -= m
            
            best_l.append(max_sum)
            
        best_l.append(0)
        
        # You care about only 1 efficiency. Check each efficiency (hince the k-1)
        return_best = 0
        for i in range(n):
            value = employees[i][0] * (employees[i][1] + best_l[i-1])
            print(value, return_best)
            if value > return_best:
                return_best = value
                
        return return_best % modulo