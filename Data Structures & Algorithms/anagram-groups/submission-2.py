from collections import Counter
class Solution:
    def checkAnagram(self, s, t):
        return dict(Counter(s)) == dict(Counter(t))
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_anagrams = []
        seen = []
        for i in range(len(strs)):
            if strs[i] in seen:
                continue
            anagrams = [strs[i]]
            for j in range(i + 1, len(strs)):
                if self.checkAnagram(anagrams[0], strs[j]):
                    anagrams.append(strs[j])
            
            all_anagrams.append(anagrams)
            seen.extend(anagrams)
        
        return all_anagrams