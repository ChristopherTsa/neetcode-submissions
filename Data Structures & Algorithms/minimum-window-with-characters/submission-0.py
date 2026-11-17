class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t):
            return ""

        char_count = {}
        for c in t:
            char_count[c] = char_count.get(c, 0) + 1

        required = len(char_count)
        formed = 0
        window_counts = {}

        l = 0
        min_len = float("inf")
        best_l, best_r = 0, 0

        for r, char in enumerate(s):
            window_counts[char] = window_counts.get(char, 0) + 1


            if char in char_count and window_counts[char] == char_count[char]:
                formed += 1

            while l <= r and formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    best_l, best_r = l, r + 1

                left_char = s[l]
                window_counts[left_char] -= 1

                if left_char in char_count and window_counts[left_char] < char_count[left_char]:
                    formed -= 1

                l += 1

        return "" if min_len == float("inf") else s[best_l:best_r]
