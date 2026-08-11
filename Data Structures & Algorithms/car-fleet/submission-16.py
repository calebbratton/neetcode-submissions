class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        seen = []
        for p, s in cars:
            ett = (target - p) / s
            seen.append(ett)
            if len(seen) > 1 and seen[-1] <= seen[-2]:
                seen.pop()

        return len(seen)