class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hash = {}
        num1=sorted(nums)
        result = []

        for i,num in enumerate(num1):
            if num not in hash:
                hash[num] = i
        for j in nums:
            result.append(hash[j])
        return result

            
            



        