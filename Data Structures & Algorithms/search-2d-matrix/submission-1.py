class Solution:
    def binarySearch(self, array: List[int], target):
        n = len(array)
        low = 0
        high = n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if array[mid] == target:
                return True
            else:
                if array[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target <= row[-1]:
                return self.binarySearch(row, target)
        
        return False