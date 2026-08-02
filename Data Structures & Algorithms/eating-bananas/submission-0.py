class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed, maxSpeed = 1, max(piles)

        result = maxSpeed
        while minSpeed <= maxSpeed:
            midSpeed = minSpeed + (maxSpeed - minSpeed) // 2

            timeToEat = 0
            for p in piles:
                timeToEat += math.ceil(float(p) / midSpeed)
            if timeToEat <= h:
                result = midSpeed
                maxSpeed = midSpeed - 1
            else:
                minSpeed = midSpeed + 1

        return result