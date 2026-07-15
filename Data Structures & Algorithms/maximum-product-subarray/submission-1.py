class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin = curMax = 1

        for n in nums:
            temp = n * curMax
            curMax = max(temp, curMin * n, n)
            curMin = min(temp, curMin * n, n)
            res = max(res, curMax)
        return res