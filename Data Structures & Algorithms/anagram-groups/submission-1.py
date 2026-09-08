#This uses sort func()-> nlogn

#Time complexity-> each element in list is being sorted => m * nlogn(m num of string and n is length of longest string)

#Space compelxity-> O (m * n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={} # hashmap<string,List<string>>
        result =[]
        for word in strs:
            sorted_list = sorted(word)
            key = "".join(sorted_list)

            if key in hm:
                hm[key].append(word)

            else:
                hm[key] = [word]  

        for i in hm:
            result.append(hm[i])

        return result    


            


        