class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n<2:
            return n

        out = 1
        
        left = 0
        count = {}
        count[s[left]] = 1

        for right in range(1, n):
            count[s[right]] = count.get(s[right], 0) + 1
            
            r = right - left + 1 - max(count.values())
            if r <= k:
                out = max(out, right - left + 1)
            else:
                while right - left + 1 - max(count.values()) > k:
                    count[s[left]] -= 1
                    left += 1
            
        return out
