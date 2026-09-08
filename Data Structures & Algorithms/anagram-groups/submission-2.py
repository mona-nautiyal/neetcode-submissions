class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for ch in word:
                indx = ord(ch) - ord('a')
                count[indx] = count[indx] + 1

            key = tuple(count) #key should be hashable, 
                               #lists are mutable so use tuple    
            hm[key].append(word)

        return  list(hm.values())