class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k= 0 
        n= len(nums)

        while k < n:
            if nums[k] == val:
                nums[k] = nums[n-1]
                n= n-1
            else:
                k = k +1
        return n


        

        


        



        