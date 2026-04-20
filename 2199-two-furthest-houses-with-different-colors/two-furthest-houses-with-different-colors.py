from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)

        dist1 = 0
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                dist1 = i
                break

        dist2 = 0
        for i in range(n):
            if colors[i] != colors[-1]:
                dist2 = n - 1 - i
                break

        return max(dist1, dist2)