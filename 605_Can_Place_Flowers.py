class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # Check if the current position is valid for planting
                if (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    n -= 1

            if n == 0:
                return True
            
        return False
    


# Example usage:
a = Solution()
print(a.canPlaceFlowers([1, 0, 0, 0, 1], 1))  # Output: True
print(a.canPlaceFlowers([1, 0, 0, 0, 1], 2))  # Output: False
