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
            if c in d.keys():
                pile.append(d[c])
            else:
                if len(pile)==0:
                    return False
                if c != pile.pop():
                    return False
        return len(pile)==0
