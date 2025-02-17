class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from itertools import permutations
        a = []
        for i in range(1, len(tiles)+1):
            a += permutations(tiles, i)

        # b = []
        # for i in a:
        #     if i not in b:    b.append(i)

        b = set(a)  # set() is faster than list() & loop for removing duplicates

        return len(b)

a = Solution()
print(a.numTilePossibilities("AAB")) # 8
print(a.numTilePossibilities("AAABBC")) # 188
print(a.numTilePossibilities("V")) # 1