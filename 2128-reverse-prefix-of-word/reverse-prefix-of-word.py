class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        index= word.find(ch)
        s1= word[:index+1]
        s2 = word[index+1:]

        return s1[: :-1]+s2


        