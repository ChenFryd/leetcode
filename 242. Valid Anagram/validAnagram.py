class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDictLetters = {}
        for letter in s:
            sDictLetters[letter] = sDictLetters.get(letter,0)+1
        
        for letter in t:
            if letter not in sDictLetters:
                return False
            sDictLetters[letter] = sDictLetters.get(letter)-1
        
        for value in sDictLetters.values():
            if value != 0:
                return False
        return True