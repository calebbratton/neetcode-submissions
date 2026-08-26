class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let seen = {}
        for (let num of nums) { 
            if (!seen[num]) {
                seen[num] = []
            }

            seen[num]++
        }

        return Object.keys(Object.fromEntries(Object.entries(seen).sort((a,b) => (b[1] - a[1])).slice(0, k)))
    }
}
