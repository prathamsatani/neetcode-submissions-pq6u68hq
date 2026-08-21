class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        count = 0
        maxCount = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                count += 1
                if count > maxCount:
                    maxCount = count
            else:
                count = 0
        
        return maxCount + 1 if len(nums) > 0 else 0