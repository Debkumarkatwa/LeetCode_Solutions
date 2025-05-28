class Solution:
    def compress(self, chars: list[str]) -> int:
        if not chars:    return
        
        compressed, count = '', 0
        alpha = chars[0]
        
        for current_char in chars:
            if current_char == alpha:
                count += 1
            else:
                compressed = compressed + alpha + str(count) if count > 1 else compressed + alpha
                alpha = current_char
                count = 1

        # Handle the last character group
        compressed = compressed + alpha + str(count) if count > 1 else compressed + alpha
            
        # Update the original list with the compressed version
        chars[:] = list(compressed)
        # Return the length of the compressed version     
        return len(compressed)
    

a = Solution()
print(a.compress(["a","a","b","b","c","c","c"]))  # Output: 6
print(a.compress(["a"]))  # Output: 1
print(a.compress(["a","b","b","b","b","b","b","b"]))  # Output: 4