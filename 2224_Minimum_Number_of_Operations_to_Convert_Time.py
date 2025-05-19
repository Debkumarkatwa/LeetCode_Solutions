class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current = int(current[:2])*60 + int(current[3:])
        correct = int(correct[:2])*60 + int(correct[3:])
        diff, op = abs(current - correct), 0

        if correct == 0 and current != 0:
            diff = 1440 - current

        # '''
        op += diff // 60
        diff -= op * 60
        
        op += diff // 15
        diff -= (diff // 15) * 15

        op += diff // 5
        diff -= (diff // 5) * 5

        op += diff # diff // 1
        return op
    
        '''          # This is the same as above but more readable 
        while diff > 0:
            if diff >= 60:
                diff -= 60
                op += 1
            elif diff >= 15:
                diff -= 15
                op += 1
            elif diff >= 5:
                diff -= 5
                op += 1
            elif diff >= 1:
                diff -= 1
                op += 1
        return op
        '''

a = Solution()
print(a.convertTime("12:01", "12:44")) # 43
print(a.convertTime("20:00", "00:00")) # 720
print(a.convertTime("00:00", "00:00")) # 0
print(a.convertTime("23:59", "00:00")) # 1
print(a.convertTime("00:00", "23:59")) # 1
print(a.convertTime("02:30", "04:35")) # 3