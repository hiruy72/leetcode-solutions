class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Count characters
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        # Check if they have the same unique characters
        if set(count1.keys()) != set(count2.keys()):
            return False
        
        # Check if their frequency counts match (after sorting)
        if sorted(count1.values()) != sorted(count2.values()):
            return False
        
        return True



        