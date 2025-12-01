class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        current_number = 1
        p =0

        while True:
            if current_number not in arr:
                p +=1
            if p == k:
                return current_number
                
            current_number +=1
        


            
         