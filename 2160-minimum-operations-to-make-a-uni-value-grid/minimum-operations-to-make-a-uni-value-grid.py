from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = [num for row in grid for num in row]
        
        # Step 1: check feasibility
        remainder = nums[0] % x
        for num in nums:
            if num % x != remainder:
                return -1
        
        # Step 2: sort
        nums.sort()
        
        # Step 3: find median
        median = nums[len(nums) // 2]
        
        # Step 4: compute operations
        operations = 0
        for num in nums:
            operations += abs(num - median) // x
        
        return operations
        