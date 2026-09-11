class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]

        pair = sorted(pair, reverse=True)

        stack = list()

        for p, s in pair:
            time_to_target = (target - p) / s

            if not stack or time_to_target > stack[-1]:
                stack.append(time_to_target)
        
        return len(stack)