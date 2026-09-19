class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30,38,30,36,35,40,28]

        # [1,4,1,2,1,0,0]

        # [1, 4, 1, 2, 1, 0, 0]

        stack = []
        res = [0] * len(temperatures) 

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                index, temp = stack.pop()
                res[index] = i - index

            stack.append([i, t])
        
        return res