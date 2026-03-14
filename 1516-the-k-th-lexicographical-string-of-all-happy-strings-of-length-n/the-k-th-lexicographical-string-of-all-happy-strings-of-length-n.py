class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        
        def backtrack(curr):
            if len(res) >= k:
                return
            
            if len(curr) == n:
                res.append(curr)
                return
            
            for ch in "abc":
                if not curr or curr[-1] != ch:
                    backtrack(curr + ch)
        
        backtrack("")
        
        if len(res) < k:
            return ""
        return res[k-1]
