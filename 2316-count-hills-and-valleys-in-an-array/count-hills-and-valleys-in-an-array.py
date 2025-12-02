class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        num  =[nums[0]]

        for n in nums[1:]:
            if n!= num[-1]:
                num.append(n)


        for i in range(1,len(num)-1):
            if num[i-1] > num[i] and num[i+1] > num[i]:
                count +=1
            if num[i-1] < num[i] and num[i+1] < num[i]:
                count +=1
        return count
            
        