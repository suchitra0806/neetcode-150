class Solution(object):
    def maxArea(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(heights) - 1
        result = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            result = max(result, area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return result
        