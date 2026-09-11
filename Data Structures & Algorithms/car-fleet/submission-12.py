class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed_position = [[p,s] for p, s in zip(position, speed)]

        res = 0
        last_fleet_time = 0

        for p, s in sorted(speed_position)[::-1]:
            time = (target - p) / s

            if res == 0 or time > last_fleet_time:
                last_fleet_time = time
                res += 1

        return res

