class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        stack = []

        for p, s in cars:
            stack.append((p, s))
            if len(stack) > 1:
                currTtf = (target - stack[-1][0]) / stack[-1][1]
                prevTtf = (target - stack[-2][0]) / stack[-2][1]
                if currTtf <= prevTtf:
                    stack.pop()
        return len(stack)