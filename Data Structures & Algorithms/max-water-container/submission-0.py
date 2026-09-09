class Solution:
    def maxArea(self, heights: List[int]) -> int:

        result = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            result = max(result, area)        

            if heights[l] < heights[r]:
                l+= 1
            elif heights[r] < heights[l]:
                r-=1
            else:
                r-=1

        return result