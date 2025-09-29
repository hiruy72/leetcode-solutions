class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # slow pointer for next non-zero position
        last_non_zero = 0
        
        # move all non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero] = nums[i]
                last_non_zero += 1
        
        # fill the rest with zeros
        for i in range(last_non_zero, len(nums)):
            nums[i] = 0
