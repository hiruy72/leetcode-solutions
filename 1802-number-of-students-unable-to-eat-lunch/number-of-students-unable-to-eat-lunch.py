class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        res = len(students)
        coun = Counter(students)

        for ch in sandwiches:
            if coun[ch] > 0:
                res -=1
                coun[ch] -=1
            else:
                return res
        return res
        