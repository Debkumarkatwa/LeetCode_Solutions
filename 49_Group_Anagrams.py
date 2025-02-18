class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        list_dict = {}
        for i in strs:
            a = ''.join(sorted(i))
            if a not in list_dict.keys():
                list_dict[a] = [i]
            else:
                list_dict[a].append(i)

        return list(list_dict.values())


a = Solution()
print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) # [["bat"],["nat","tan"],["ate","eat","tea"]]
