from datetime import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1, date2 = date1.split('-'), date2.split('-')
        date1, date2 = datetime(int(date1[0]), int(date1[1]), int(date1[2])), datetime(int(date2[0]), int(date2[1]), int(date2[2]))
        return abs((date1 - date2).days)

a = Solution()
print(a.daysBetweenDates(date1 = "2019-06-29", date2 = "2019-06-30")) # 1
print(a.daysBetweenDates(date1 = "2020-01-15", date2 = "2020-12-31")) # 15
