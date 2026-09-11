# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         output = []
#         for i, n in enumerate(nums):
#             p = 1
#             for j in range(len(nums)):
#                 if j!=i:
#                     p *= nums[j]
            
#             output.append(p)

#         return output

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        #[1,2,4,6]

        i = 1
        while i<len(nums):
            output[i] = nums[i-1] * output[i-1]
            i+=1
        
        # Right now i = len 
        # We can start at second last element since last element doesn't have postfix
        i -=2
        postfix_p = 1
        while i>=0:
            postfix_p *= nums[i+1]
            output[i] *= postfix_p
            i-=1

        return output
            



