class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip trailing spaces, split by spaces
        words = s.strip().split()
        # Return length of last word if exists, else 0
        return len(words[-1]) if words else 0
