class Solution:
    def rotatedDigits(self, n: int) -> int:
        def is_good(num):
            has_changed = False
            
            while num > 0:
                d = num % 10
                
                if d in [3, 4, 7]:
                    return False
                if d in [2, 5, 6, 9]:
                    has_changed = True
                
                num //= 10
            
            return has_changed
        
        count = 0
        for i in range(1, n + 1):
            if is_good(i):
                count += 1
        
        return count
        