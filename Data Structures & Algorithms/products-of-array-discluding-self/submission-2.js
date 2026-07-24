class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const result = nums
        let maxProduct = 1
        let zeroCount = 0

        for (let num of nums) {
            if (num === 0) {
                zeroCount++
            } else {
                maxProduct *= num
            }
        }

        if (zeroCount > 1) {
            return result.fill(0, 0, nums.length)
        }
        for (let i = 0; i < nums.length; i++) {
            if (zeroCount > 0) {
                if (nums[i] === 0) {
                    result[i] = maxProduct
                } else {
                    result[i] = 0
                }
            } else {
                result[i] = maxProduct / nums[i]
            }
        }

        return result
    }
}
