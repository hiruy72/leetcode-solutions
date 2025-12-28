class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize the result list with zeros
        res = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # The number of 1s in i is the same as i//2 plus i%2
            res[i] = res[i >> 1] + (i & 1)
        
        return res
