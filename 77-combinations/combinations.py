class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, path):
            # If combination is complete
            if len(path) == k:
                res.append(path[:])
                return
            
            # Try each number from start to n
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()  # backtrack

        backtrack(1, [])
        return res
