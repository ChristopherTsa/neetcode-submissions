class Solution:

    def encode(self, strs: List[str]) -> str:
        header = ",".join(str(len(s)) for s in strs)
        return f"{header}#{''.join(strs)}"

    def decode(self, s: str) -> List[str]:
        sep = s.find("#")
        header = s[:sep]
        if not header:
            return []
        
        lengths = [int(x) for x in header.split(",")]
        res = []
        idx = sep + 1
        for length in lengths:
            res.append(s[idx : idx + length])
            idx += length
        return res
