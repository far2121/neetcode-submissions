class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = {}

        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        for count in freq.values():
            if count % 2 != 0:
                return False

        return True