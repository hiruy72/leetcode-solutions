class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s = set(arr)
        current_number = 1
        p =0

        while True:
            if current_number not in s:
                p +=1
            if p == k:
                return current_number
                
            current_number +=1
        


            
         