class Solution:
    def binarySearch(self, nums, left, right, target):
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            else:
                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
        return -1
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            comp = target - numbers[i]
            if comp > numbers[-1]:
                continue
            j = self.binarySearch(numbers, i + 1, len(numbers) - 1, comp)
            if j != -1:
                return [i + 1, j + 1]
        
        return [-1, -1]
