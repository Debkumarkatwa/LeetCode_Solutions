class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index, max_length = {}, 0
        start = 0
        for i, char in enumerate(s):
            if char in index and index[char] >= start:
                start = index[char] + 1

            index[char] = i
            max_length = max(max_length, i - start + 1)

        return max_length

# Example usage
a = Solution()
print(a.lengthOfLongestSubstring('abcabcbb'))   # 3
print(a.lengthOfLongestSubstring('bbbbb'))      # 1
print(a.lengthOfLongestSubstring('pwwkew'))     # 3