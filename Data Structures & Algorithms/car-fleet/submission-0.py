class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []

        for position, speed in sorted(pair, reverse=True):
            time = (target-position)/speed

            if stack and time <= stack[-1]:
                continue

            stack.append(time)
        
        return len(stack)
        
