class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort()
        result = [folder[0]]

        for f in folder[1:]:
            if not f.startswith(result[-1] + '/'):
                result.append(f)
        return result


a = Solution()
print(a.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))
print(a.removeSubfolders(["/a","/a/b/c", "/a/b/d", "/a/b/c/d"]))
print(a.removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"]))