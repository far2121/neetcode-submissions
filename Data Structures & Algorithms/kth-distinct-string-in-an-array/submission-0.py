class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}

        #count freq of each string
        for s in arr:
            freq[s] = freq.get(s, 0) + 1

        #find kth string
        for s in arr:
            if freq[s] == 1:
                k -= 1
                if k == 0:
                    return s
        return ""        