class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n

        for i in range(n):
            left[i] = max(left[i - 1], height[i]) if i > 0 else height[i]
        
        for j in range(n - 1, -1, -1):
            right[j] = max(right[j + 1], height[j]) if j < n - 1 else height[j]
        
        water = 0
        for i in range(n):
            water += min(left[i], right[i]) - height[i]

        return water