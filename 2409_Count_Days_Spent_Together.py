from datetime import datetime
class Solution:
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 0 is a placeholder as the month is 1-indexed
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def days(date: str) -> int:
            date = datetime.strptime(date, "%m-%d")
            return sum(self.month[:date.month]) + date.day
        
        arriveAlice = days(arriveAlice)
        leaveAlice = days(leaveAlice)
        arriveBob = days(arriveBob)
        leaveBob = days(leaveBob)
        
        if max(arriveAlice, arriveBob) > min(leaveAlice, leaveBob): return 0
        return min(leaveAlice, leaveBob) - max(arriveAlice, arriveBob) + 1
        
    
a = Solution()
print(a.countDaysTogether(arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19")) # 3
print(a.countDaysTogether(arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31")) # 0