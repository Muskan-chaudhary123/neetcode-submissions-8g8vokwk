from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for st in strs:
            dic[tuple(sorted(st))].append(st)
        
        return list(dic.values())