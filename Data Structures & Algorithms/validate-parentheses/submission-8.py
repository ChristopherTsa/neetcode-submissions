class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        
        d = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        pile = []

        for c in s:
            if c in d:
                pile.append(d[c])
            elif not pile or c != pile.pop():
                return False

        return len(pile)==0
