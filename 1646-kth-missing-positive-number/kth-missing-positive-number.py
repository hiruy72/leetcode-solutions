class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        seen = set(arr)
        miss_count = 0
        current_number = 1

        while True:
            if current_number not in seen:
                miss_count +=1
                if miss_count == k:
                    return current_number
            current_number +=1
        return


        



        