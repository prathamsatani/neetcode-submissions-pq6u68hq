class Solution:
    def maxArea(self, heights: list[int]) -> int:
        i, j = 0, len(heights) - 1
        maxA = float("-inf")
        while i <= j:
            curA = min(heights[i], heights[j]) * (j - i)
            if curA > maxA:
                maxA = curA
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return maxA