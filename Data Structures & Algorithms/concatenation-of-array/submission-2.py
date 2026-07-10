class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        ans[:] = nums
        ans.extend(nums)
        return ans