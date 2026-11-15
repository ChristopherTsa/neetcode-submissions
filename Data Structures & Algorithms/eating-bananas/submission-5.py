class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left <= right:
            mid = left + (right - left) // 2
            time = 0
            for pile in piles:
                time += pile//mid
                if pile%mid>0:
                    time +=1
            if time <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left