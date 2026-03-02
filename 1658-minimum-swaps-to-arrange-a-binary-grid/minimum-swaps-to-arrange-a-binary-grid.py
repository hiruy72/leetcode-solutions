class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Count trailing zeros for each row
        trailing_zeros = []
        for row in grid:
            count = 0
            for num in reversed(row):
                if num == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)
        
        swaps = 0
        
        for i in range(n):
            required = n - i - 1
            j = i
            
            # Find a row with enough trailing zeros
            while j < n and trailing_zeros[j] < required:
                j += 1
            
            if j == n:
                return -1  # Not possible
            
            # Bring row j up to position i
            while j > i:
                trailing_zeros[j], trailing_zeros[j - 1] = trailing_zeros[j - 1], trailing_zeros[j]
                swaps += 1
                j -= 1
        
        return swaps
        