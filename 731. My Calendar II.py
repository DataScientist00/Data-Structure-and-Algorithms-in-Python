# problem link-->> https://leetcode.com/problems/my-calendar-ii/description/


class MyCalendarTwo:

    def __init__(self):
        self.calender = []
        self.overlap = []
        
    def book(self, st: int, et: int) -> bool:
        if len(self.calender) == 0:
            self.calender.append((st,et))
            return True
        for l ,r in self.overlap:
            if not (et <= l or st >= r):
                return False
        for l ,r in self.calender:
            if not(et <= l or st >= r):
                self.overlap.append((max(l,st) , min(et,r)))
        
        self.calender.append((st,et))
        return True
            

        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
