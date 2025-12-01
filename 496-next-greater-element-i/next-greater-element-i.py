class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        # Step 1: Compute next greater for nums2
        for num in nums2:
            while stack and num > stack[-1]:
                top = stack.pop()
                next_greater[top] = num
            stack.append(num)

        # Remaining numbers have no next greater
        for num in stack:
            next_greater[num] = -1

        # Step 2: Build result for nums1
        return [next_greater[num] for num in nums1]





        