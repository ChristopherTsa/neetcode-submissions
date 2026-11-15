from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = defaultdict(list)

        for s in strs:
            cle = frozenset(Counter(s).items())
            mem[cle].append(s)

        return list(mem.values())
