class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [(index, temp)]

        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                res[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            
            stack.append((i, temp))
        
        return res

            