class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        return[celsius + 273.15 , celsius * 1.80 + 32.00]
    



a = Solution()
print(a.convertTemperature(celsius = 36.50))  # [309.65000,97.70000]
print(a.convertTemperature(celsius = 122.11))  # [395.26000,251.79800]