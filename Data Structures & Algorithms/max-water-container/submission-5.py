class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        left = 0
        right = n-1

        out = 0

        while left < right:
            vol = min(heights[left], heights[right]) * (right - left)
            if vol > out:
                out = vol

            if heights[right] < heights[left]:
                right -=1
            else:
                left +=1

        return out


        