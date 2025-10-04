class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for word in strs:
            # Sort the word to use as a key
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)
        
        # Return grouped anagrams
        return list(anagrams.values())
