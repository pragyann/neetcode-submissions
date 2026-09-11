class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            m_val = nums[m]

            if target == m_val:
                return m
            
            if m_val >= nums[l]:
                print("left sorted array", m_val, nums[l])
                if target < m_val and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target > m_val and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            print(l, r)
                
        return -1
        