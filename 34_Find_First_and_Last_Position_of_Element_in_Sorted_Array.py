class Solution:
    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        result = []
        for query in queries:
            a = s[query[0]:query[1]+1]
            left, right = a.find('|'), a.rfind('|')
            result.append(a[left:right].count('*'))

        return result

a = Solution()
print(a.platesBetweenCandles(s = "**|**|***|", queries = [[2,5],[5,9]]))    # [2,3]
print(a.platesBetweenCandles(s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]))     # [9,0,0,0,0]