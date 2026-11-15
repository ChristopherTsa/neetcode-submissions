class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        out = 0
        
        n = len(s)
        if n < 2:
            return n
        
        left = 0
        right = 1
        
        mem = {}
        mem[s[left]] = 1

        while left < n and right < n:
            mem[s[right]] = mem.get(s[right], 0) + 1
            
            while mem[s[right]] > 1:
                mem[s[left]] -= 1
                left += 1
            
            right += 1
            out = max(out, right - left)

        return out
        



