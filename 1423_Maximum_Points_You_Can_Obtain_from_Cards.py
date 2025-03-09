class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        left = max_score = sum(cardPoints[:k])  # sum of first k elements (assummend as max points)   `[1+2+3]`
        right = 0  # sum of last k elements (assummend as 0)  `[]`
        for i in range(1,k+1):
            left -= cardPoints[k-i]  # remove last k'th element from left  ` [1+2+3] -> [1+2] -> [1] -> [] `
            right += cardPoints[-i]  # and add i'th last element from right  ` [] -> [1] -> [1+6] -> [1+6+5] `
            max_score = max(max_score, left+right)
        return max_score
    

a = Solution()
print(a.maxScore(cardPoints = [1,2,3,4,5,6,1], k = 3)) # 12
print(a.maxScore(cardPoints = [2,2,2], k = 2)) # 4
print(a.maxScore(cardPoints = [9,7,7,9,7,7,9], k = 7)) # 55