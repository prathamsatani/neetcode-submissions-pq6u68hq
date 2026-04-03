class Solution:
    def search(self, arr: List[int], left: int, right: int, tgt: int) -> int:
        while left <= right:
            mid = left + int((right - left)/2)
            if arr[mid] == tgt:
                return mid
            else:
                if tgt < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx1 in range(len(numbers)):
            tgt = target - numbers[idx1]
            idx2 = self.search(numbers, idx1 + 1, len(numbers) - 1, tgt)
            if idx2 > 0 and idx1 < idx2:
                return [idx1 + 1, idx2 + 1]
        
        return [-1, -1]