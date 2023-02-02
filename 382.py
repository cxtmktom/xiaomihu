from collections import Counter



class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = Counter([i for i in ransomNote])
        mag = Counter([i for i in magazine]) # big
        print(mag - ran)

        for k,v in ran.items():
            if k not in mag:
                return False
            elif v > mag[k]:
                return False
        return True


Solution().canConstruct("aa","aba")

