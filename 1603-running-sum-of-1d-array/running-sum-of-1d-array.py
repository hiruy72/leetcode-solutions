class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [nums[0]]
        for i in range(1,len(nums)):
            sum =0
            for j in range(i+1):
                sum += nums[j]
            result.append(sum)
        return result



        
        
            

        