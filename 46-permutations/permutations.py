class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        res = []
        
        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])  # append a copy
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # swap
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # backtrack (swap back)
        
        backtrack(0)
        return res
