class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = [c.lower() for c in s if c.isalnum()]
        print(t)
        r = t[::-1]
        print(r)

        return "".join(r)=="".join(t)