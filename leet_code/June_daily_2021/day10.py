from sortedcontainers import SortedList
class MyCalendar:
    
    isBetweenStart = lambda self, x, y, z: x <= y < z 
    isBetweenEnd = lambda self, x, y, z: x < y < z 
    
    def __init__(self):
        self.schedule = SortedList([])

    def book(self, start: int, end: int) -> bool:
        for interval in self.schedule:
            s, e = interval
            if (self.isBetweenStart(s, start, e) or self.isBetweenEnd(s, end, e)) or \
               (self.isBetweenStart(start, s, end) or self.isBetweenEnd(start, e, end)):
                return False
        
        self.schedule.add((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)