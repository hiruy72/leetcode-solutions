class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        r1= []
        r2= []

        for i in s:
            if i == "#" and r1:
                r1.pop()
            elif i != "#":
                r1.append(i)
        for j in t:
            if j == "#" and  r2:
                r2.pop()
            elif j != "#":
                r2.append(j)
        return r1==r2

        
        