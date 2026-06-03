class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl=sorted(s)
        tl=sorted(t)
        if (sl==tl):
            return True
        return False
