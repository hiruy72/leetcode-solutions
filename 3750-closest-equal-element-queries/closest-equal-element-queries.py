from typing import List
from collections import defaultdict
import bisect

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        pos = defaultdict(list)

        # store all indices for each value
        for i, v in enumerate(nums):
            pos[v].append(i)

        # precompute best distance for each index
        best = [-1] * n

        for v, idxs in pos.items():
            m = len(idxs)
            if m == 1:
                continue

            for j in range(m):
                cur = idxs[j]
                prev = idxs[j - 1]
                nxt = idxs[(j + 1) % m]

                d1 = abs(cur - prev)
                d1 = min(d1, n - d1)

                d2 = abs(cur - nxt)
                d2 = min(d2, n - d2)

                best[cur] = min(d1, d2)

        return [best[i] for i in queries]