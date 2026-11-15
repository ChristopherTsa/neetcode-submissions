class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        out = 0
        if not nums:
            return out
        
        numSet = set(nums)
        
        for i in nums:
            if (i-1) not in numSet:
                l = 1
                n = 1
                while (i+n) in numSet:
                    l += 1
                    n += 1
                if l>out:
                    out = l
        return out 

        
