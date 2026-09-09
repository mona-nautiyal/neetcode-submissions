class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        length = len(nums)
        result = [1] * length
        after_prod = 1
        before_prod = 1

       #created prefix array
        for idx in range(0,len(nums)):
            result[idx] *= before_prod 
            before_prod *= nums[idx]
            
        #use suffix var to store running product    
        for idx in range(len(nums)-1, -1, -1):
            result[idx] *=  after_prod
            after_prod *= nums[idx]

        return result    
            




    
       



        