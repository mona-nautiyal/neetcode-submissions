class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        result = []

        for num in nums:
            hm[num] += 1 

        sorted_list = sorted(
                            hm.items(), 
                            key = lambda x: x[1], 
                            reverse= True
                        )    
        for i in range(k):
            result.append(sorted_list[i][0])                

        return result        
