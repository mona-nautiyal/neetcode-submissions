class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {} #space complexity= O(K)

        for char in s:   #Time Complexity = O(N)
            hm[char] = hm.get(char,0)+1

        for char in t:    #Toime complexity = O(M)
            val = hm.get(char,0)

            # Why to check further
            if val==0:
                return False

            hm[char] = val - 1
            
            if hm[char]==0:
                del hm[char]

        if not hm:
            return True

        return False            

            