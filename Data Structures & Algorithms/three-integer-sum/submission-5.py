class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        out = []

        if n < 3:
            return out
        

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            k = nums[i]
            right = n-1
            left = i+1
            while left < right:
                l = nums[left]
                r = nums[right]
                if l + r + k > 0:
                    right -= 1
                elif l + r + k < 0:
                    left += 1
                elif l + r + k==0:
                    out.append([k, l, r])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return out

        