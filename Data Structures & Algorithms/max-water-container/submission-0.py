#Here I used Brute Force Method 
"""

"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_water_area = 0

        for i in range(n):
            for j in range(i + 1, n):
                width = j - i
                height = min(heights[i], heights[j])

                area = width * height

                if area > max_water_area:
                    max_water_area = area

        return max_water_area

#This has time complexity of O(n**2)
