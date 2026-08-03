class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.helper(nums[1:]), self.helper(nums[:-1]), nums[0])

    def helper(self, nums):
        house1, house2 = 0, 0

        for i in nums:
            temp = max(i + house1, house2)
            house1 = house2
            house2 = temp
        return house2