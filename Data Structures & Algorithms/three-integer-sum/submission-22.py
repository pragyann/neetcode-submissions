class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1, 0, 1, 2, -1, -4]
        # [-4, -1, -1, -1, 0, 1, 2, 2] -> -1 + (-1+2)
                   
        # (-1, -1, 2), (-1, 0, 1)
        # 

        res = []
        nums.sort()

        for i in range(len(nums)-2):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                sum = nums[i] + nums[l] + nums[r]

                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    while r > l and nums[r] == nums[r+1]:
                        r -= 1
            
            i += 1

        return res