class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedd={}
        for i in strs:
            val="".join(sorted(i))
            if val in sortedd:
                sortedd[val].append(i)
            else:
                sortedd[val]=[i]
        return list(sortedd.values())