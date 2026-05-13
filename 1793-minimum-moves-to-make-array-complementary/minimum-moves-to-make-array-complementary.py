class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        # difference array
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b) + 1
            high = max(a, b) + limit
            s = a + b

            # initially assume 2 moves
            diff[2] += 2

            # one move range starts
            diff[low] -= 1

            # zero move at exact sum
            diff[s] -= 1
            diff[s + 1] += 1

            # back to 2 moves after high
            diff[high + 1] += 1

        ans = float('inf')
        curr = 0

        for target in range(2, 2 * limit + 1):
            curr += diff[target]
            ans = min(ans, curr)

        return ans
        