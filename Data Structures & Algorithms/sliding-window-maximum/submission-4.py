# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         q = collections.deque()

#         res = []

#         for i in range(0, len(nums)):
#             if q and q[0] == i - k:
#                 q.popleft()

#             while q and nums[q[-1]] < nums[i]:
#                 q.pop()
            
            
#             q.append(i)

#             if i >= k - 1:
#                 res.append(nums[q[0]])
        
#         return res
    
#     # By maintaining this structure, each element is added and removed at most once, giving an optimal solution.
#     # And hence the time complexity is O(n + n) = O(n) and not O(n*k).




class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
            res = []

            q = collections.deque()

            for i, n in enumerate(nums):
                
                while q and nums[q[-1]] < n:
                    q.pop()
                
                q.append(i)

                if q[0] <= i - k:
                    q.popleft()
                
                if i >= k - 1:
                    res.append(nums[q[0]])

            return res

                


                




























            



