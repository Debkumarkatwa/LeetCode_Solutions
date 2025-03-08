class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        a = []
        for i in range(len(blocks) - k + 1):
            a.append(blocks[i:i+k].count('W'))
        return min(a)
    

a = Solution()
print(a.minimumRecolors(blocks = "WBBWWBBWBW", k = 7))  # 3
print(a.minimumRecolors(blocks = "WBWBBBW", k = 2))  # 0