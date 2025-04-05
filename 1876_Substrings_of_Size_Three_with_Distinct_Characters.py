class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = int()
        for i in range(len(s) - 2):
            if s[i] != s[i+1] and s[i+1] != s[i+2] and s[i+2] != s[i]:
                count += 1
                
        return count
        

a = Solution()
print(a.countGoodSubstrings('xyzzaz')) # 1
print(a.countGoodSubstrings('aababcabc')) # 4