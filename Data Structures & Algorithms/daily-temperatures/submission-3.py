class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [[i, temperature]]
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):

            while stack and stack[-1][1] < t:
                popped_i, popped_t = stack.pop()
                distance = i - popped_i
                res[popped_i] = distance    

            stack.append([i, t])
        
        return res
