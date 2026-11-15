class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n

        prefixe = 1
        for i in range(n):
            out[i] *= prefixe
            prefixe *= nums[i]
        
        suffixe = 1
        for i in reversed(range(n)):
            out[i] *= suffixe
            suffixe *= nums[i]

        return out
            

