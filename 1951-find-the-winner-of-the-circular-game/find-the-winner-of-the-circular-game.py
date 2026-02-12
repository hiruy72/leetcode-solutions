class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        result = [i for i in range(1,n +1 )]
        curr =0

        while len(result) > 1:
            curr = (curr + k -1 )% len(result)
            result.pop(curr)
        return result[0]


        
        