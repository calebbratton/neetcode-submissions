class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        k = len(nums)-1
        used = defaultdict(bool)
        for i, n in enumerate(nums):
            j, k = i + 1, len(nums)-1
            while j < k:
                current = n + nums[j] + nums[k]
                if current == 0:
                    using = str(n) + str(nums[j]) + str(nums[k])
                    if not used[using]:
                        result.append([n, nums[j], nums[k]])
                        used[using] = True

                if current < 0:
                    j += 1
                else:
                    k -= 1

        return result