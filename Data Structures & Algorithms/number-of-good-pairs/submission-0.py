class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}
        pairs = 0

        for x in nums:
            if x in freq:
                pairs += freq[x]
                freq[x] += 1
            else:
                freq[x] = 1

        return pairs