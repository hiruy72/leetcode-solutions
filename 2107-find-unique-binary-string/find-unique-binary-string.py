from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        # Convert list to a set for O(1) lookups
        num_set = set(nums)
        
        # Try all possible binary strings of length n
        for i in range(2**n):
            candidate = bin(i)[2:].zfill(n)  # binary string padded to length n
            if candidate not in num_set:
                return candidate